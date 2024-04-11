#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import Session
from sqlalchemy.orm import relationship
from sqlalchemy import VARCHAR, Column, String
from os import getenv
import models
from models.city import City


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'
    id = Column(VARCHAR(60), primary_key=True)
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state",
                          cascade="all, delete")
    #@property
    #def cities(self):
    #    """Getter attribute cities that
    #eturns the list of City instances"""
        #city_list = []
        #all_cities = models.storage.all(City)
        #for city in all_cities.values():
        #    if city.state_id == self.id:
        #   city_list.append(city)
        #return city_list

    if getenv('HBNB_TYPE_STORAGE') != 'db':
        @property
        def cities(self):
            """Returns the list of City instances with
            state_id equals to the current State.id"""
            from models import storage
            all_cities = storage.all(City)
            return [city for city in all_cities.values()
                    if city.state_id == self.id]

        def close(self):
            """Close session"""
            Session.close()