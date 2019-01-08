#!/usr/bin/python3
"""This is the amenity class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Amenity(BaseModel, Base):
    """This is the class for Amenity
    Attributes:
        name: input name
    """
    __tablename__ = 'amenities'
    name = Column('name', String(128), nullable=False)

    # @property
    # def amenities(self):
    #     return self.amenities

    # @amenities.setter
    # def amenities(self, amenities):
    #     if
    #     self.amenities = amenities
