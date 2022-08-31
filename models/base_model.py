#!/usr/bin/python3
# base_model.py
"""Defines the BaseModel class"""
from types import ClassMethodDescriptorType
import uuid
from datetime import datetime

class BaseModel:
        """Represents a BaseModel object"""

        def __init__(self):
                """Initializes a BaseClass instance"""
                self.id = str(uuid.uuid4())
                self.created_at = datetime.now()
                self.updated_at = datetime.now()

        def __str__(self):
                """prints class name and attributes"""
                return (f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}")

        def save(self):
                """updates the current instance attributes"""
                self.updated_at = datetime.now()
        
        def to_dict(self):
                """returns a dictionary containing all key/values of __dict__ of the instance"""
                d = self.__dict__
                d['__class__'] = self.__class__.__name__
                d['created_at'] = str(self.created_at.strftime('%Y-%m-%dT%H:%M:%S.%f'))
                d['updated_at'] = str(self.updated_at.strftime('%Y-%m-%dT%H:%M:%S.%f'))
                return d

b = BaseModel()
b.name = "John"
b.age = 20
# print(b)
# b.save()
# print(b)
print(len(b.id))
b_json = b.to_dict()
print(b_json)
print('JSON of b:')
for key in b_json.keys():
        print("\t{}: ({}) - {}".format(key, type(b_json[key]), b_json[key]))