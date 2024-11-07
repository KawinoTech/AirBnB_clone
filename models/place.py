#!/usr/bin/python3
"""
This module defines the Place class, which inherits from BaseModel.
The Place class represents a rental property or location in the application
and includes attributes for location, amenities, and other relevant details.

Classes:
    Place: Inherits from BaseModel and defines additional attributes
    specific to place information.
"""

from models.base_model import BaseModel


class Place(BaseModel):
    """
    Place class that inherits from BaseModel. Represents a rental place
    or property with specific attributes such as location and amenities.

    Attributes:
        city_id (str): ID of the city where the place is located.
        name (str): Name of the place. Defaults to an empty string.
        description (str): Description of the place. Defaults empty string.
        number_rooms (int): Number of rooms in the place.
        number_bathrooms (int): Number of bathrooms in the place.
        max_guest (int): Maximum number of guests the place can accommodate.
        price_by_night (int): Price per night to rent the place.
        latitude (float): Latitude coordinate of the place.
        longitude (float): Longitude coordinate of the place.
        amenity_ids (list): List of amenity IDs associated with the place.
    """

    city_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
