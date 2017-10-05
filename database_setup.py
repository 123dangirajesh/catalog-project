from sqlalchemy import Column, ForeignKey, Integer, String, DateTime, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from datetime import datetime


Base = declarative_base()


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    created_date = Column(DateTime, default=func.current_timestamp())
    name = Column(String(2500), nullable=False)
    email = Column(String(2500), nullable=False)


class Level(Base):
    __tablename__ = 'level'

    id = Column(Integer, primary_key=True)
    name = Column(String(2500), nullable=False)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)
    excercise = relationship('Excercise', cascade='all, delete-orphan')

    # We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'Level': self.name,
            'id': self.id,
        }


class Excercise(Base):
    __tablename__ = 'excercise'

    id = Column(Integer, primary_key=True)
    name = Column(String(2500), nullable=False)
    created_date = Column(DateTime, default=func.current_timestamp())
    description = Column(String(10000))
    provider = Column(String(2500))
    link = Column(String(2500))
    level_id = Column(Integer, ForeignKey('level.id'))
    level = relationship(Level)
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship(User)

    # We added this serialize function to be able to send JSON objects in a serializable format
    @property
    def serialize(self):
        """Return object data in easily serializeable format"""
        return {
            'excercise name': self.name,
            'description': self.description,
            'provider': self.provider,
            'id': self.id,
        }


engine = create_engine('postgresql://catalog:catalog@catalog/catalog')

Base.metadata.create_all(engine)
