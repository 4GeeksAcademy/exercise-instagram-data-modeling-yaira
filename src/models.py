import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'User'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    LastName = Column(String(50), nullable=False)
    userName = Column(String(50), nullable=False)
    email = Column(String(50), nullable=False)

class Follower(Base):
    __tablename__ = 'Follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer,ForeignKey('User.id'))

class Comments(Base):
    __tablename__ = 'Comments'
    id = Column(Integer, primary_key=True)
    comment_Text = Column(String(250))
    User_id = Column(Integer, ForeignKey('User.id'))
    Post_id = Column(Integer, ForeignKey('Posts.id'))

class Posts(Base):
    __tablename__ = 'Posts'
    id = Column(Integer, primary_key=True)
    User_id = Column(Integer, ForeignKey('User.id'))

class Media(Base):
    __tablename__ = 'Media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('Posts.id'))
    url = Column(String(250), nullable=False)



    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
