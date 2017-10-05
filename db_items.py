from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Level, Base, Excercise, User


engine = create_engine('postgresql://catalog:catalog@catalog/catalog')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
# A DBSession() instance established
session = DBSession()

# Creating dummy user
User = User(name="Rajesh", email="dangirajesh19971@gmail.com",)
session.add(User)
session.commit()

# Levels
easy = Level(user_id=1, name="Easy")
session.add(easy)
session.commit()

medium = Level(user_id=1, name="Medium")
session.add(medium)
session.commit()

difficult = Level(user_id=1, name="Difficult")
session.add(difficult)
session.commit()

# easy exercies

excercise = Excercise(user_id=1,
    name="pushups(knee)",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="mountain climbers",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="box jumps",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="jumping jacks",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="bicycle crunches",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="plank",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="knee kicks",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="high knees",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="quick punches",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="uppercuts",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://google.com",
    provider="My self",
    level=easy)
session.add(excercise)
session.commit()





# medium exercies

excercise = Excercise(user_id=1,
    name="pushups hip touches",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="burpee",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="burpee(+hill climb)",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="crab walk",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="inverted rows",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="sprawls",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="pullups",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="bench dips",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="plank to pushups ",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://www.google.com",
    provider="My self",
    level=medium)
session.add(excercise)
session.commit()


# Difficult excerises

excercise = Excercise(user_id=1,
    name="T-plank pushups",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=difficult)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="sit thurst",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=difficult)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="pullup bar crunches",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=difficult)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="leg raises",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=difficult)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="pistol squat",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=difficult)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="Tyson-neck raise",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi. """,
    link="https://www.google.com",
    provider="My self",
    level=difficult)
session.add(excercise)
session.commit()

excercise = Excercise(user_id=1,
    name="prisoner squat",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=difficult)
session.add(excercise)
session.commit()


excercise = Excercise(user_id=1,
    name="180 jump squat",
    description="""Lorem ipsum dolor sit amet, consectetur adipiscing elit. Fusce vitae erat sed libero rhoncus sodales at tincidunt urna. Vestibulum malesuada ante at urna gravida iaculis. Nulla eu elit nec magna fermentum venenatis quis vehicula tortor. Vivamus sollicitudin nunc at blandit iaculis. Integer congue lorem sed leo congue, a pellentesque quam dapibus. Cras consequat turpis lectus, sit amet lobortis odio sollicitudin eget. Integer rutrum elementum justo quis maximus. Phasellus consectetur, elit vitae scelerisque varius, ipsum massa interdum ipsum, eget pretium dolor erat a ligula. Proin sed sem molestie, tempus odio ut, feugiat dolor. Fusce pretium commodo consectetur. Nulla facilisi.""",
    link="https://www.google.com",
    provider="My self",
    level=difficult)
session.add(excercise)
session.commit()
print ("added Excercise!")
