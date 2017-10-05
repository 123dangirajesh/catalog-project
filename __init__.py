from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, make_response
from flask import session as login_session
from sqlalchemy import create_engine, asc, desc, DateTime, func
from sqlalchemy.orm import sessionmaker
from oauth2client.client import flow_from_clientsecrets
from oauth2client.client import FlowExchangeError
from .database_setup import Base, Level, Excercise, User
from functools import wraps
import random, string, httplib2, json, requests

app = Flask(__name__)
app.secret_key = 'super_secret_key'

# Update client_secrets.json with your Google API project information.
# Do not change this assignment.
CLIENT_ID = json.loads(
    open('/var/www/html/catalog/catalog/client_secrets.json', 'r').read())['web']['client_id']
APPLICATION_NAME = "Catalog App"

# Connect to Database and create database session
engine = create_engine('postgresql://catalog:catalog@catalog/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()



# Login decorator for checking if user is logged in or not
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'username' not in login_session:
            return redirect('/login')
        return f(*args, **kwargs)
    return decorated_function


# Create anti-forgery state token
@app.route('/login')
def showLogin():
    """This function creates an anti-forgery
        state token and renders login page """
    state = ''.join(random.choice(
                   string.ascii_uppercase + string.digits) for x in range(32))
    login_session['state'] = state
    return render_template('login.html', STATE=state)


@app.route('/gconnect', methods=['POST'])
def gconnect():
    """Exchange the one-time authorization code for a token and
        store the token in the session."""
    # Validate state token
    if request.args.get('state') != login_session['state']:
        response = make_response(json.dumps('Invalid state parameter.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    # Obtain authorization code, now compatible with Python3
    request.get_data()
    code = request.data.decode('utf-8')

    try:
        # Upgrade the authorization code into a credentials object
        oauth_flow = flow_from_clientsecrets('client_secrets.json', scope='')
        oauth_flow.redirect_uri = 'postmessage'
        credentials = oauth_flow.step2_exchange(code)
    except FlowExchangeError:
        response = make_response(
            json.dumps('Failed to upgrade the authorization code.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Check that the access token is valid.
    access_token = credentials.access_token
    url = ('https://www.googleapis.com/oauth2/v1/tokeninfo?access_token=%s'
           % access_token)
    # Submit request, parse response - Python3 compatible
    h = httplib2.Http()
    response = h.request(url, 'GET')[1]
    str_response = response.decode('utf-8')
    result = json.loads(str_response)

    # If there was an error in the access token info, abort.
    if result.get('error') is not None:
        response = make_response(json.dumps(result.get('error')), 500)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is used for the intended user.
    gplus_id = credentials.id_token['sub']
    if result['user_id'] != gplus_id:
        response = make_response(
            json.dumps("Token's user ID doesn't match given user ID."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Verify that the access token is valid for this app.
    if result['issued_to'] != CLIENT_ID:
        response = make_response(
            json.dumps("Token's client ID does not match app's."), 401)
        response.headers['Content-Type'] = 'application/json'
        return response

    stored_access_token = login_session.get('access_token')
    stored_gplus_id = login_session.get('gplus_id')
    if stored_access_token is not None and gplus_id == stored_gplus_id:
        response = make_response(json.dumps(
                            'Current user is already connected.'), 200)
        response.headers['Content-Type'] = 'application/json'
        return response

    # Store the access token in the session for later use.
    print(access_token)
    login_session['access_token'] = access_token
    login_session['gplus_id'] = gplus_id

    # Get user info
    userinfo_url = "https://www.googleapis.com/oauth2/v1/userinfo"
    params = {'access_token': access_token, 'alt': 'json'}
    answer = requests.get(userinfo_url, params=params)

    data = answer.json()

    login_session['username'] = data['name']
    login_session['picture'] = data['picture']
    login_session['email'] = data['email']

    # checking whether user exists, if not then make a new user
    user_id = getUserID(login_session['email'])
    if not user_id:
        user_id = createUser(login_session)
    login_session['user_id'] = user_id

    output = ''
    output += '<h3>Welcome, '
    output += login_session['username']
    output += '!</h3>'
    flash("Welcome ! You are now logged in as %s" % login_session['username'])
    return output

# User Helper Functions


def createUser(login_session):
    """Create new User if it does exists in the database"""
    newUser = User(name=login_session['username'], email=login_session[
                   'email'])
    session.add(newUser)
    session.commit()
    user = session.query(User).filter_by(email=login_session['email']).one()
    return user.id


def getUserInfo(user_id):
    """Extracting User data from database"""
    user = session.query(User).filter_by(id=user_id).one()
    return user


def getUserID(email):
    """Extracting email of user if it is present in the database"""
    try:
        user = session.query(User).filter_by(email=email).one()
        return user.id
    except:
        return None

# DISCONNECT - Revoke a current user's token and reset their login_session


@app.route('/gdisconnect')
def gdisconnect():
    access_token = login_session.get('access_token')
    print('Access Token')
    if access_token is None:
        print('Access Token is None')
        response = make_response(json.dumps('Current user not connected.'), 401)
        response.headers['Content-Type'] = 'application/json'
        return response
    url = 'https://accounts.google.com/o/oauth2/revoke?token=%s' % access_token
    h = httplib2.Http()
    result = h.request(url, 'GET')[0]
    print('result')
    if result['status'] == '200':
        # Reset the user's sesson.
        del login_session['access_token']
        del login_session['gplus_id']
        del login_session['username']
        del login_session['email']
        del login_session['picture']

        return redirect(url_for('showLevels'))
    else:
        # For whatever reason, the given token was invalid.
        response = make_response(json.dumps('Failed to revoke token for given user.', 400))
        response.headers['Content-Type'] = 'application/json'
        return response


# show all levels
@app.route('/')
def showLevels():
    """renders main page which displays latest content added to the database"""
    levels = session.query(Level).all()
    Excercises = session.query(Excercise).order_by(
                     func.DateTime(Excercise.created_date)).limit(9).all()
    # Checks if user in session and renders page accordingly.
    if 'username' not in login_session:
        return render_template('public_levels.html',
                               levels=levels, Excercises=Excercises)
    else:
        return render_template('member_levels.html',
                               levels=levels, Excercises=Excercises)


# Show existing Excercise in a level
@app.route('/<path:level_name>/')
def showLevel(level_name):
    """This renders Excercises present in particular category"""
    levels = session.query(Level).all()
    level = session.query(Level).filter_by(name=level_name).one()
    Excercises = session.query(Excercise).filter_by(level_id=level.id).all()
    if 'username' not in login_session:
        return render_template('public_level.html',
                               levels=levels, Excercise=Excercise, level=level)
    else:
        return render_template('member_level.html',
                               levels=levels, Excercise=Excercise, level=level)


# Show Excercise infomation
@app.route('/<path:level_name>/<path:Excercise_name>/')
def showExcercise(level_name, excercise_name):
    """Showing Excercise information"""
    level = session.query(Level).filter_by(name=level_name).one()
    excercise = session.query(Excercise).filter_by(name=excercise_name).one()
    if 'username' not in login_session:
        return render_template('public_Excercise.html',
                               Excercise=Excercise, level=level)
    else:
        return render_template('member_Excercise.html',
                               Excercise=Excercise, level=level)


# add new Excercise
@app.route('/excercise/new/', methods=['GET', 'POST'])
@login_required
def newExcercise():
    """add a new Excercise"""
    if request.method == 'POST':
        level = session.query(Level).filter_by(
            name=request.form['level']).one()
        newExcercise = Excercise(name=request.form['name'],
                           provider=request.form['provider'],
                           link=request.form['link'],
                           description=request.form['description'],
                           user_id=login_session['user_id'],
                           level_id=level.id)
        session.add(newExcercise)
        session.commit()
        flash('New Excercise %s Successfully Created' % newExcercise.name)
        return redirect(url_for('showLevel', level_name=level.name))
    else:
        return render_template('new_Excercise.html')


# Edit existing Excercise
@app.route('/<path:level_name>/<path:Excercise_name>/edit/',
           methods=['GET', 'POST'])
@login_required
def editExcercise(level_name, Excercise_name):
    """Edit an existing Excercise"""
    level = session.query(Level).filter_by(name=level_name).one()
    Excercise = session.query(Excercise).filter_by(name=Excercise_name).one()
    # If user is in session but is not creator of Excercise than
    # this checks that and prompts user with not authorized message
    if Excercise.user_id != login_session['user_id']:
        return
    
    if request.method == 'POST':
        if request.form['name']:
            Excercise.name = request.form['name']
        if request.form['description']:
            Excercise.description = request.form['description']
        if request.form['provider']:
            Excercise.provider = request.form['provider']
        if request.form['link']:
            Excercise.link = request.form['link']
        if request.form['level']:
            new_level = session.query(Level).filter_by(
                name=request.form['level']).one()
            Excercise.level_id = new_level.id
        session.add(Excercise)
        session.commit()
        flash('Excercise Successfully Edited')
        return redirect(url_for('showLevel', level_name=level_name))
    else:
        return render_template('edit_Excercise.html', Excercise=Excercise, level=level)


# Delete existing Excercise
@app.route('/<path:level_name>/<path:Excercise_name>/delete/',methods=['GET', 'POST'])
@login_required
def deleteExcercise(level_name, Excercise_name):
    """Delete an existing Excercise"""
    level = session.query(Level).filter_by(name=level_name).one()
    Excercise = session.query(Excercise).filter_by(name=Excercise_name).one()
    # If user is in session but is not creator of Excercise than this checks that and prompts user with not authorized message
    if Excercise.user_id != login_session['user_id']:
        return
    
    if request.method == 'POST':
        session.delete(Excercise)
        session.commit()
        flash('Excercise Successfully Deleted')
        return redirect(url_for('showLevels'))
    else:
        return render_template('delete_Excercise.html',
                               level=level, Excercise=Excercise)


# JSON APIs to view Excercise Catalog Information
@app.route('/level/JSON/')
def levelsJSON():
    """This outputs entire level table as json data"""
    levels = session.query(Level).all()
    return jsonify(levels=[level.serialize for level in levels])


@app.route('/level/<path:level_name>/JSON/')
def levelJSON(level_name):
    """This outputs all the Excercises present
         in a particular level as json data"""
    print(level_name)
    level = session.query(Level).filter_by(name=level_name).one()
    Excercises = Excercises.query(Excercise).filter_by(level_id=level.id).all()
    return jsonify(excercise=[i.serialize for i in excercises])


@app.route('/level/<path:level_name>/<path:Excercise_name>/JSON/')
def excerciseJSON(level_name, Excercise_name):
    """This outputs particular Excercise as json data"""
    level = session.query(Level).filter_by(name=level_name).one()
    Excercises = session.query(Excercise).filter_by(name=Excercise_name).all()
    return jsonify(Excercise=[i.serialize for i in Excercises])


if __name__ == '__main__':
    app.secret_key = 'super_secret_key'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
