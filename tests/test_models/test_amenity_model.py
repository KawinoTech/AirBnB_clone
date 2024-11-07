#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""

import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for the Amenity class.
    """

    def setUp(self):
        """Set up test environment for each test method."""
        self.amenity = Amenity()

    def test_instance_creation(self):
        """
        Test that an Amenity instance is created successfully.
        Check that it is an instance of both Amenity and BaseModel.
        """
        self.assertIsInstance(self.amenity, Amenity)
        self.assertIsInstance(self.amenity, BaseModel)

    def test_default_attributes(self):
        """
        Test that the name attribute defaults to an empty string.
        """
        self.assertEqual(self.amenity.name, "")

    def test_name_assignment(self):
        """
        Test setting the name attribute on an Amenity instance.
        """
        self.amenity.name = "Pool"
        self.assertEqual(self.amenity.name, "Pool")

    def test_unique_id(self):
        """
        Test that each Amenity instance has a unique ID.
        """
        amenity2 = Amenity()
        self.assertNotEqual(self.amenity.id, amenity2.id)

    def test_to_dict_contains_class(self):
        """
        Test that the dictionary representation of Amenity includes the '__class__' key.
        """
        amenity_dict = self.amenity.to_dict()
        self.assertIn("__class__", amenity_dict)
        self.assertEqual(amenity_dict["__class__"], "Amenity")

    def test_str_representation(self):
        """
        Test the string representation of the Amenity instance.
        It should follow the format: [ClassName] (id) {attributes}.
        """
        expected_str = f"[Amenity] ({self.amenity.id}) {self.amenity.__dict__}"
        self.assertEqual(str(self.amenity), expected_str)

    def test_save_updates_updated_at(self):
        """
        Test that calling save() updates the updated_at attribute.
        """
        old_updated_at = self.amenity.updated_at
        self.amenity.save()
        self.assertNotEqual(self.amenity.updated_at, old_updated_at)
        self.assertGreater(self.amenity.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
