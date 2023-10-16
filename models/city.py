#!/usr/bin/python3
"""This module creates a User class city"""

from models.base_model import BaseModel


class City(BaseModel):
    """Class for managing city objects
       state_id: str(empty string)
       name: string thats enpty

    """

    state_id = ""
    name = ""
