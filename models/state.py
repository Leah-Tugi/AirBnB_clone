#!/usr/bin/python3
"""This module creates n define a User class"""

from models.base_model import BaseModel


class State(BaseModel):
    """Class for managing state objects

        class attributes:
            name: string empty
    """

    name = ""
