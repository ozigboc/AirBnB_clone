#!/usr/bin/python3
# file_storage.py
"""Module to Create the FileStorage class"""
import json
from models.base_model import BaseModel

class FileStorage:
        """Represents a FileStorage objects"""
        __file_path = 'file.json'
        __objects = {}

        def all(self):
                """Returns the dictionary objects"""
                return self.__objects

        def new(self, obj):
                """Sets in __objects the obj with key <obj class key>.id"""
                self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

        def save(self):
                """serializes __objects to the JSON path"""
                d = {}
                for key, value in self.__objects.items():
                        d[key] = value.to_dict()
                with open(self.__file_path, 'a') as f:
                        json.dump(d, f)

        def reload(self):
                """Deserializes the JSON file to __objects"""
                try:
                        f = open(self.__file_path, 'r')
                        d = json.load(f)
                        for k, v in d.items():
                                self.__objects[k] = BaseModel(**v)
                except FileNotFoundError:
                        pass


class MyEncoder(json.JSONEncoder):
        def default(self, obj):
                return obj.__dict__

