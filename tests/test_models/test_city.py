#!/usr/bin/python3
"""
This module contains unittests for City class
"""
from models.base_model import BaseModel
from models.city import City
import unittest


class TestCity(unittest.TestCase):
    """Defines test cases for City class"""

    def test_init(self):
        """Test Initialization"""
        inst = City()
        inst.id = "11111111-2222-2222-2222-333333444444"
        inst.name = "lagos"
        self.assertEqual(inst.id, "11111111-2222-2222-2222-333333444444")
        self.assertEqual(inst.name, "lagos")

    def test_subclass(self):
        """Tests if city is a subclass of the BaseModel class"""
        city = City()
        self.assertIsInstance(city, BaseModel)
        self.assertTrue(hasattr(city, "id"))
        self.assertTrue(hasattr(city, "created_at"))

    def test_city_attribute(self):
        """Tests the attributes of the City class"""
        city = City()
        self.assertTrue(hasattr(city, "name"))
        self.assertEqual(city.name, "")
        self.assertTrue(hasattr(city, "state_id"))
        self.assertEqual(city.state_id, "")

    def test_to_dict_values(self):
        """Tests dict values returned from to_dict call"""
        city = City()
        new_dict = city.to_dict()
        format = "%Y-%m-%dT%H:%M:%S.%f"
        self.assertEqual(new_dict["__class__"], "City")
        self.assertEqual(type(new_dict["created_at"]), str)
        self.assertEqual(type(new_dict["updated_at"]), str)
        self.assertEqual(new_dict["created_at"],
                         city.created_at.strftime(format))
        self.assertEqual(new_dict["updated_at"],
                         city.updated_at.strftime(format))
