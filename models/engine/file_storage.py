#!/usr/bin/python3
# file_storage.py
"""Module to Create the FileStorage class"""
import json
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models.user import User


classes = {
    "Amenity": Amenity, "State": State, "User": User,
    "Place": Place, "Review": Review, "City": City,
    "BaseModel": BaseModel
}


class FileStorage:
    """Represents a FileStorage objects"""
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class key>.id"""
        if obj:
            self.__objects[f"{obj.__class__.__name__}.{obj.id}"] = obj

    def save(self):
        """serializes __objects to the JSON path"""
        d = {}
        for key, value in self.__objects.items():
            d[key] = value.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(d, f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, 'r') as f:
                d = json.load(f)
                for k, v in d.items():
                    classname = v.get('__class__')
                    self.__objects[k] = classes[classname](**v)
        except FileNotFoundError:
            pass
