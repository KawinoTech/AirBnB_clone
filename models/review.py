#!/usr/bin/python3
"""
This module defines the Review class, which inherits from BaseModel.
The Review class represents a user review for a specific place and
includes attributes such as the place ID, user ID, and review text.

Classes:
    Review: Inherits from BaseModel and defines additional attributes
    specific to review information.
"""

from models.base_model import BaseModel


class Review(BaseModel):
    """
    Review class that inherits from BaseModel. Represents a user review
    for a place with attributes for associated
    place, user, and review content.

    Attributes:
        place_id (str): The ID of the place
        being reviewed. Defaults empty string.
        user_id (str): The ID of the user who
        submitted the review. Defaults empty string.
        text (str): The content of the review. Defaults to an empty string.
    """

    place_id = ""
    user_id = ""
    text = ""
