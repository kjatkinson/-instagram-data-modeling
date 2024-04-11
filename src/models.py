import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)

    comments = relationship("Comment")
    posts = relationship("Post")
    media = relationship("Media")
    def to_dict(self):
        return {}

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    street_name = Column(String(250))
    street_number = Column(String(250))
    post_code = Column(String(250), nullable=False)

    comments = relationship("Comment")
    posts = relationship("Post")
    media = relationship("Media")
    def to_dict(self):
        return {}

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    text = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))

    comments = relationship("Comment,followers")
    posts = relationship("Post, followers")
    media = relationship("Media, followers")
    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    title = Column(String(250))
    user_id = Column(Integer, ForeignKey('user.id'))

    comments = relationship("Comment")
    posts = relationship("Post")
    media = relationship("Media")
    def to_dict(self):
        return {}

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250))
    url = Column(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

    comments = relationship("Comment")
    posts = relationship("Post")
    media = relationship("Media")
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem generating the diagram")
    raise e