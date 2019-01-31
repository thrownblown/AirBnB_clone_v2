#!/usr/bin/python3
"""This is the state class"""
import models
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os


class State(BaseModel, Base):
    """This is the class for State
    Attributes:
        name: input name
    """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="all, delete")
    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """ cities getter from FS
            """
            objs = models.storage.all(City)
            return ([c for c in objs if objs[c].state_id == self.id])
