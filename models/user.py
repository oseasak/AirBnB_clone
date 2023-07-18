#!/usr/bin/python3
from models.base_model import BaseModel

"""Defining the User class."""

class User(BaseModel):
    """Represent a User.
    Attributes:
        email: The email of the user.
        password: The password of the user.
        first_name: The first name of the user.
        last_name: The last name of the user.
    """

    email = ""
    password = ""
    first_name = ""
    last_name = ""
