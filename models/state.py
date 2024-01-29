#!/usr/bin/python3
""" stattte Module for HBNB pro"""
from os import environ

from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from models.base_model import Base, BaseModel
import models

from models.city import City


class State(BaseModel, Base):
    """ State CLLASS """

    if environ.get('HBNB_TYPE_STORAGE') == 'db':

        __tablename__ = "states"
        name = Column(String(128), nullable=False)

        cities = relationship("City",
                              backref="state",
                              cascade="all, delete-orphan",
                              passive_deletes=True)
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """initializes state"""
        super().__init__(*args, **kwargs)

    if environ.get('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Return list of citites

            
            """
            return [city for city in models.storage.all(
                City).values() if city.state_id == self.id]

