xc#!/usr/bin/python3
"""This is the place class"""
from sqlalchemy import Column, String, ForeignKey, Integer, Float
from models.base_model import BaseModel, Base
from sqlalchemy.ext.declarative import declarative_base


class Place(BaseModel, Base):
    """This is the class for Place
    Attributes:
        city_id: city id
        user_id: user id
        name: name input
        description: string of description
        number_rooms: number of room in int
        number_bathrooms: number of bathrooms in int
        max_guest: maximum guest in int
        price_by_night:: pice for a staying in int
        latitude: latitude in flaot
        longitude: longitude in float
        amenity_ids: list of Amenity ids
    """
    __tablename__ = 'places'
    city_id = Column('city_id', String(60), nullable=False,
                     ForeignKey('cities.id'))
    user_id = Column('user_id', String(60), nullable=False,
                     ForeignKey('users.id'))
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024))
    number_rooms = Column('number_rooms', Integer, default=0, nullable=False)
    number_bathrooms = Column('number_bathroom', Integer, default=0,
                              nullable=False)
    max_guest = Column('max_guest', Integer, default=0, nullable=False)
    price_by_night = Column('price_by_night', Integer, default=0,
                            nullable=False)
    latitude = Column('latitude', Float, default=0, nullable=False)
    longitude = Column('latitude', Float, default=0, nullable=False)
    amenity_ids = []
