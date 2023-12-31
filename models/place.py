#!/usr/bin/python3
""" Place Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column
from sqlalchemy import Float
from sqlalchemy import ForeignKey
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy.orm import relationship
import os
from sqlalchemy import Table
from models.amenity import Amenity
from models.review import Review


class Place(BaseModel):
    """ A place to stay """

    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024), nullable=False)
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    """
    amenity_ids = []

    reviews = relationship("Review", backref="place", cascade="delete")
    amenities = relationship("Amenity", secondary="place_amenity",
                             viewonly=False)

    """create relationship Many-To-Many between Place and Amenity"""
    table = Table("place_amenity", Base.metadata,
                          Column("place_id", String(60),
                              ForeignKey("places.id"), 
                              primary_key=True, nullable=False),
                          Column("amenity_id", String(60),
                              ForeignKey("amenities.id"),
                              primary_key=True, nullable=False))
    
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            review = list()
            for value in models.storage.all(Review).items():
                if value.place_id == self.id:
                    review.append(value)
            return review
        @property
        def amenities(self):
            amenity = list()
            for value in models.storage.all(Amenity).items():
                if amenity.id in self.amenity_ids:
                    amenity.append(value)
            return amenity

        @amenities.setter
        def amenities(self, value):
            if type(value) == Amenity:
                self.amenity_ids.append(value.id)
