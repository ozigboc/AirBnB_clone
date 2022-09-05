#!/usr/bin/python3
# base_model.py
"""Defines the BaseModel class"""

import uuid
import models
from datetime import datetime


class BaseModel:
    """Represents a BaseModel object"""

    def __init__(self, *args, **kwargs):
        """Initializes a BaseClass instance"""
        if len(args) != 0:
            raise TypeError("Too many arguments")

        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    setattr(self, key, datetime.fromisoformat(value))
                else:
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        """prints class name and attributes"""
        return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """updates the current instance attributes"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns a dictionary containing all key/values of
                __dict__ of the instance
        """

        d = self.__dict__.copy()
        d["__class__"] = self.__class__.__name__
        if "created_at" in d:
            d["created_at"] = str(
                self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'))
        if "updated_at" in d:
            d["updated_at"] = str(
                self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'))
        return d
