#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
from os import getenv


class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = "states"
    if getenv("HBNB_TYPE_STORAGE") == "db":
        name = Column(String(128), nullable=False)
        cities = relationship('City', backref='state', cascade='all, delete')
    else:
        name = ""

    @property
    def cities(self):
        """Function for cities"""
        city_list = [city for city in storage.all(
            City).values() if city.state_id == self.id]
        return city_list
