#!/usr/bin/python3
# city.py
"""Defines a City Model class"""
from models.base_model import BaseModel


class City(BaseModel):
    """Represent a city Model"""
    state_id = ""
    name = ""
