#!/usr/bin/python3
"""
Unit tests for the City class.
"""

import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test cases for the City class.
    """

    def setUp(self):
        """Set up test environment for each test method."""
        self.city = City()

    def test_instance_creation(self):
        """
        Test that a City instance is created successfully.
        Check that it is an instance of both City and BaseModel.
        """
        self.assertIsInstance(self.city, City)
        self.assertIsInstance(self.city, BaseModel)

    def test_default_attributes(self):
        """
        Test the default values of the name and state_id attributes.
        They should both be empty strings by default.
        """
        self.assertEqual(self.city.name, "")
        self.assertEqual(self.city.state_id, "")

    def test_name_assignment(self):
        """
        Test setting the name attribute on a City instance.
        """
        self.city.name = "San Francisco"
        self.assertEqual(self.city.name, "San Francisco")

    def test_state_id_assignment(self):
        """
        Test setting the state_id attribute on a City instance.
        """
        self.city.state_id = "CA123"
        self.assertEqual(self.city.state_id, "CA123")

    def test_unique_id(self):
        """
        Test that each City instance has a unique ID.
        """
        city2 = City()
        self.assertNotEqual(self.city.id, city2.id)

    def test_to_dict_contains_class(self):
        """
        Test that the dictionary representation of City includes the '__class__' key.
        """
        city_dict = self.city.to_dict()
        self.assertIn("__class__", city_dict)
        self.assertEqual(city_dict["__class__"], "City")

    def test_str_representation(self):
        """
        Test the string representation of the City instance.
        It should follow the format: [ClassName] (id) {attributes}.
        """
        expected_str = f"[City] ({self.city.id}) {self.city.__dict__}"
        self.assertEqual(str(self.city), expected_str)

    def test_save_updates_updated_at(self):
        """
        Test that calling save() updates the updated_at attribute.
        """
        old_updated_at = self.city.updated_at
        self.city.save()
        self.assertNotEqual(self.city.updated_at, old_updated_at)
        self.assertGreater(self.city.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
