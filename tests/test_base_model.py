#!/usr/bin/python3
"""Module for testing BaseModel class"""
import unittest
from models.base_model import BaseModel


class TestBaseModel(unittest.TestCase):
    """Suite to test BaseModel class"""

    def test_id(self):
        """Test assigned id"""
        test_obj = BaseModel()
        self.assertIsNotNone(test_obj.id)

    def test_id_length(self):
        """Test if id was correctly generated"""
        test_obj = BaseModel()
        id_len = 36
        self.assertEqual(id_len, len(test_obj.id))
