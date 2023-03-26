#!/usr/bin/python3
"""Place Module for HBNB project"""
import models
from models.base_model import BaseModel, Base
from models.review import Review
from models.amenity import Amenity
from sqlalchemy import Column, String, Integer, Float, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv


"""Relation many-to-many"""
metadata = Base.metadata
place_amenity = Table("place_amenity", metadata,
                      Column("place_id", String(60),
                             ForeignKey("places.id"),
                             primary_key=True,
                             nullable=False),
                      Column("amenity_id", String(60),
                             ForeignKey("amenities.id"),
                             primary_key=True,
                             nullable=False))


class Place(BaseModel, Base):
    """A place to stay"""
    __tablename__ = "places"
    city_id = Column(String(60), ForeignKey("cities.id"), nullable=False)
    user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
    name = Column(String(128), nullable=False)
    description = Column(String(1024))
    number_rooms = Column(Integer, nullable=False, default=0)
    number_bathrooms = Column(Integer, nullable=False, default=0)
    max_guest = Column(Integer, nullable=False, default=0)
    price_by_night = Column(Integer, nullable=False, default=0)
    latitude = Column(Float)
    longitude = Column(Float)
    amenity_ids = []
    reviews = relationship("Review", cascade="delete", backref="place")
    amenities = relationship(
        "Amenity", secondary="place_amenity",
        viewonly=False, back_populates="place_amenities")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def reviews(self):
            """Getter for the review class"""
            reviews_list = []
            for review_obj in models.storage.all(Review).values():
                if self.id == review_obj.place_id:
                    reviews_list.append(review_obj)
            return reviews_list

        @property
        def amenities(self):
            """Getter for the amenity class"""
            amenities_list = []
            for amenity_obj in models.storage.all(Amenity).values():
                if amenity_obj.id in amenities_list:
                    amenities_list.append(amenity_obj)
            return amenities_list

        @amenities.setter
        def amenities(self, value):
            """Setter for the amenities class"""
            if value.__class__ == Amenity:
                self.amenity_ids.append(value.id)
