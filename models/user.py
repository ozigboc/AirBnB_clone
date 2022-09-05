#!/usr/bin/python3
# user.py
"""Defines the User model class that inherits from BaseModel class"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    Represents a user model class

    Attrs:
        email: string - email of user
        password: string - password of user
        first_name: string - first_name of user
        last_name: string - last_name of user
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
