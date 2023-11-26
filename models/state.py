#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
import os

class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    """ for dbstorage"""
    cities = relationship("City", backref='state', cascade="all, delete")
    """
    name = ""
    """
    """returns the list of City instances with state_id"""
    if os.getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            city = list()
            for value in models.storage.all(city).items():
                if value.state_id == self.id:
                    city.append(value)
            return city

