#!/usr/bin/python3
"""This module creates or defines a Review class"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class for managing review objects
         place_id string:empty
         user_id string that is empty
         text: empty string
    """

    place_id = ""
    user_id = ""
    text = ""
