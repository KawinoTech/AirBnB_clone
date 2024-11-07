#!/usr/bin/python3
"""
This module defines the City class, which inherits from BaseModel.
The City class represents a city in the application and includes
basic attributes such as name and state_id.

Classes:
    State: Inherits from BaseModel and defines additional attributes
    specific to user information.
"""

from models.base_model import BaseModel


class City(BaseModel):
    """
    User class that inherits from BaseModel. Represents a user with
    the following attributes:

    Attributes:
        name (str): The last name of the user. Defaults to an
                         empty string.
        state_id (str): state id from State class instance
    """
    name = ""
    state_id = ""
