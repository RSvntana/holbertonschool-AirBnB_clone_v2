#!/usr/bin/python3
""" User Module for HBNB project """
from models.base_model import BaseModel
from models.review import Review
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship


class User(BaseModel):
    """ User class """
    __tablename__ = 'users'

    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    reviews = relationship('Review', backref='user', cascade='all, delete')
