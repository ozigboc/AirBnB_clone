"""
This module defines unittests for the Amenity Model class
"""
from models.amenity import Amenity
from models.base_model import BaseModel
import unittest


class TestAmenity(unittest.TestCase):
    """Test the Amenity class"""

    def test_is_subclass(self):
        """Test that Amenity is a subclass of the BaseModel Class"""
        amenity = Amenity()
        self.assertIsInstance(amenity, BaseModel)
        self.assertTrue(hasattr(amenity, "id"))
        self.assertTrue(hasattr(amenity, "created_at"))
        self.assertTrue(hasattr(amenity, "updated_at"))

    def test_name_attr(self):
        """Test that Amenity has attribute name"""
        amenity = Amenity()
        self.assertTrue(hasattr(amenity, "name"))
        self.assertEqual(amenity.name, "")

    def test_to_dict_creates_dict(self):
        """test the to_dict method creates a dictionary"""
        amenity_ins = Amenity()
        new_dictionary = amenity_ins.to_dict()
        self.assertEqual(type(new_dictionary), dict)
        self.assertFalse("_sa_instance_state" in new_dictionary)
        for attr in amenity_ins.__dict__:
            if attr != "_sa_instance_state":
                self.assertTrue(attr in new_dictionary)
        self.assertTrue("__class__" in new_dictionary)

    def test_to_dict_values(self):
        """test values in the dict returned from to_dict func are correct"""
        t_format = "%Y-%m-%dT%H:%M:%S.%f"
        amenity_ins = Amenity()
        new_dictionary = amenity_ins.to_dict()
        self.assertEqual(new_dictionary["__class__"], "Amenity")
        self.assertEqual(type(new_dictionary["created_at"]), str)
        self.assertEqual(type(new_dictionary["updated_at"]), str)
        self.assertEqual(
            new_dictionary["created_at"],
            amenity_ins.created_at.strftime(t_format))
        self.assertEqual(
            new_dictionary["updated_at"],
            amenity_ins.updated_at.strftime(t_format))

    def test_str(self):
        """test that the str method has the correct output"""
        amenity = Amenity()
        string = "[Amenity] ({}) {}".format(amenity.id, amenity.__dict__)
        self.assertEqual(string, str(amenity))
