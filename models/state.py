#!/usr/bin/python3
""" State Module for HBNB project """
import models
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship
from os import getenv


class State(BaseModel, Base):
    """State class"""
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="delete", backref="state")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Getter for the city class"""
            cities_list = []
            for city_obj in models.storage.all(City).values():
                if self.id == city_obj.state_id:
                    cities_list.append(city_obj)
            return cities_list
