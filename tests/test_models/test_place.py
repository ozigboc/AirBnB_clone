#!/usr/bin/python3
"""
This module contains unittests for Place class
"""
from models.base_model import BaseModel
from models.place import Place
import unittest


class TestPlace(unittest.TestCase):
    """Defines test cases for Place class"""

    def test_subclass(self):
        """Tests that the Place class is a subclass of the BaseModel class"""
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertTrue(hasattr(place, "id"))
        self.assertTrue(hasattr(place, "created_at"))
        self.assertTrue(hasattr(place, "updated_at"))

    def test_init(self):
        """Test Initialization"""
        inst = Place()
        inst.city_id = "11111111-2222-2222-2222-333333888888"
        inst.user_id = "11111111-2222-2222-2222-333333999999"
        inst.name = "Bole"
        inst.description = "random description"
        inst.amenity_ids = ["Bole"]
        self.assertEqual(inst.city_id, "11111111-2222-2222-2222-333333888888")
        self.assertEqual(inst.user_id, "11111111-2222-2222-2222-333333999999")
        self.assertEqual(inst.name, "Bole")
        self.assertEqual(inst.description, "random description")
        self.assertEqual(inst.number_rooms, 0)
        self.assertEqual(inst.number_bathrooms, 0)
        self.assertEqual(inst.max_guest, 0)
        self.assertEqual(inst.price_by_night, 0)
        self.assertEqual(inst.latitude, 0.0)
        self.assertEqual(inst.longitude, 0.0)
        self.assertEqual(inst.amenity_ids[0], "Bole")

    def test_str(self):
        """test that the str method"""
        place = Place()
        string = "[Place] ({}) {}".format(place.id, place.__dict__)
        self.assertEqual(string, str(place))
