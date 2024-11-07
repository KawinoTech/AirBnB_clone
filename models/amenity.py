#!/usr/bin/python3
"""
This module defines the Amenity class, which inherits from BaseModel.
The Amenity class represents an amenity in the application and includes
basic attributes such as name.

Classes:
    State: Inherits from BaseModel and defines additional attributes
    specific to user information.
"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    User class that inherits from BaseModel. Represents a user with
    the following attributes:

    Attributes:
        name (str): The last name of the user. Defaults to an
                         empty string.
    """
    name = ""
