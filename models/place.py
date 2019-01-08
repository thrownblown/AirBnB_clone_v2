#!/usr/bin/python3
"""This is the place class"""
import os
from sqlalchemy import Column, String, ForeignKey, Integer, Float, Table
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


metadata = Base.metadata
place_amenity = Table('place_amenity', metadata,
                Column('place_id',
                        String(60),
                        primary_key=True,
                        nullable=False),
                Column('amenity_id',
                        String(60),
                        ForeignKey("amenities.id"),
                        primary_key=True,
                        nullable=False)
                )

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
    city_id = Column('city_id', String(60),
                    ForeignKey('cities.id'), nullable=False)
    user_id = Column('user_id', String(60),
                    ForeignKey('users.id'), nullable=False)
    name = Column('name', String(128), nullable=False)
    description = Column('description', String(1024))
    number_rooms = Column('number_rooms', Integer, default=0, nullable=False)
    number_bathrooms = Column('number_bathroom', Integer, default=0,
                    nullable=False)
    max_guest = Column('max_guest', Integer, default=0, nullable=False)
    price_by_night = Column('price_by_night', Integer, default=0,
                            nullable=False)
    latitude = Column('latitude', Float, default=0, nullable=False)
    longitude = Column('longitude', Float, default=0, nullable=False)
    amenities = relationship("Amenity", secondary=place_amenity,
                            backref='places', viewonly=False)

    if os.getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def amenities(self):
            """ amenities getter for FS
            """
            # objs = storage.all(City)
            # return ([c for c in objs if c.state_id == self.id])
            pass

