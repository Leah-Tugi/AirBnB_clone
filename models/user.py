#!/usr/bin/python3
"""This module createsand defines a User class"""
from models.base_model import BaseModel


class User(BaseModel):
    """Class for managing user objects
        email: mpty str
        password: empty str
        first_name: pty str
        last_name : empty str
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
