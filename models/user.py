#!/usr/bin/python3
"""This is the user class"""
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base
import os
import models

class User(BaseModel, Base):
    """This is the class for user
    Attributes:
        email: email address
        password: password for you login
        first_name: first name
        last_name: last name
    """
    __tablename__ = 'users'
    email = Column('email', String(128), nullable=False)
    password = Column('password', String(128), nullable=False)
    first_name = Column('first_name', String(128), nullable=False, default='John')
    last_name = Column('last_name', String(128), nullable=False, default='Doe')
    places = relationship("Place", backref="user")
    reviews = relationship("Review", backref="user")

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def reviews(self):
            """ review getter from FS
            """
            objs = models.storage.all(Review)
            return ([r for r in objs if r.user_id == self.id])
