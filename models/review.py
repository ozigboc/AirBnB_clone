#!/usr/bin/python3
# review.py
"""Defines a Review Model Class"""
from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a review Model"""
    place_id = ""
    user_id = ""
    text = ""
