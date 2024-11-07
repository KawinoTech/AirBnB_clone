#!/usr/bin/python3
"""
Unit tests for the Place class.
"""

import unittest
from models.place import Place
from models.base_model import BaseModel


class TestPlace(unittest.TestCase):
    """
    Test cases for the Place class.
    """

    def setUp(self):
        """Set up test environment for each test method."""
        self.place = Place()

    def test_instance_creation(self):
        """
        Test that a Place instance is created successfully.
        Check that it is an instance of both Place and BaseModel.
        """
        self.assertIsInstance(self.place, Place)
        self.assertIsInstance(self.place, BaseModel)

    def test_default_attributes(self):
        """
        Test that all default attributes are correctly initialized.
        """
        self.assertEqual(self.place.city_id, "")
        self.assertEqual(self.place.name, "")
        self.assertEqual(self.place.description, "")
        self.assertEqual(self.place.number_rooms, 0)
        self.assertEqual(self.place.number_bathrooms, 0)
        self.assertEqual(self.place.max_guest, 0)
        self.assertEqual(self.place.price_by_night, 0)
        self.assertEqual(self.place.latitude, 0.0)
        self.assertEqual(self.place.longitude, 0.0)
        self.assertEqual(self.place.amenity_ids, [])

    def test_attribute_types(self):
        """
        Test that all attributes have the expected types.
        """
        self.assertIsInstance(self.place.city_id, str)
        self.assertIsInstance(self.place.name, str)
        self.assertIsInstance(self.place.description, str)
        self.assertIsInstance(self.place.number_rooms, int)
        self.assertIsInstance(self.place.number_bathrooms, int)
        self.assertIsInstance(self.place.max_guest, int)
        self.assertIsInstance(self.place.price_by_night, int)
        self.assertIsInstance(self.place.latitude, float)
        self.assertIsInstance(self.place.longitude, float)
        self.assertIsInstance(self.place.amenity_ids, list)

    def test_unique_id(self):
        """
        Test that each Place instance has a unique ID.
        """
        place2 = Place()
        self.assertNotEqual(self.place.id, place2.id)

    def test_name_assignment(self):
        """
        Test setting the name attribute on a Place instance.
        """
        self.place.name = "Seaside Villa"
        self.assertEqual(self.place.name, "Seaside Villa")

    def test_to_dict_contains_class(self):
        """
        Test that the dictionary representation of Place includes the '__class__' key.
        """
        place_dict = self.place.to_dict()
        self.assertIn("__class__", place_dict)
        self.assertEqual(place_dict["__class__"], "Place")

    def test_str_representation(self):
        """
        Test the string representation of the Place instance.
        It should follow the format: [ClassName] (id) {attributes}.
        """
        expected_str = f"[Place] ({self.place.id}) {self.place.__dict__}"
        self.assertEqual(str(self.place), expected_str)

    def test_save_updates_updated_at(self):
        """
        Test that calling save() updates the updated_at attribute.
        """
        old_updated_at = self.place.updated_at
        self.place.save()
        self.assertNotEqual(self.place.updated_at, old_updated_at)
        self.assertGreater(self.place.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
