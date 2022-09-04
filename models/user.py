#!/usr/bin/python3
# user.py
"""Defines the User model class that inherits from BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Represents a user model class"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
