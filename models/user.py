#!/usr/bin/python3
"""
This module defines the User class, which inherits from BaseModel.
The User class represents a user in the application and includes
basic attributes such as email, password, first name, and last name.

Classes:
    User: Inherits from BaseModel and defines additional attributes
    specific to user information.
"""

from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that inherits from BaseModel. Represents a user with
    the following attributes:

    Attributes:
        email (str): The email address of the user. Defaults to an
                     empty string.
        password (str): The password of the user. Defaults to an empty
                        string.
        first_name (str): The first name of the user. Defaults to an
                          empty string.
        last_name (str): The last name of the user. Defaults to an
                         empty string.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
