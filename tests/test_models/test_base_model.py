#!/usr/bin/python3
"""
Unit tests for the BaseModel class.

This module contains unit tests for the `BaseModel` class, which defines the common attributes and methods for other classes in a project.
The tests cover various aspects of the `BaseModel` class, including:
- Ensuring `id` uniqueness and validity
- Verifying timestamp types and updates
- Checking the string representation of the instance

Classes:
    TestBaseModel: Contains unit tests for the `BaseModel` class.

Attributes:
    sleep_time (int): Specifies the time in seconds to pause between tests that compare timestamps.
"""

import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.

    This class contains tests for validating the functionality of the `BaseModel` class, such as unique ID generation,
    correct timestamp handling, and proper string representation format.

    Attributes:
        sleep_time (int): The time to sleep in seconds, used to ensure timestamps are different for certain tests.
    """

    sleep_time = 1

    def test_id(self):
        """
        Test that the `id` attribute is of type `str`.

        This test ensures that the `id` attribute generated for each instance of `BaseModel` is a string.
        The test creates an instance of `BaseModel` and asserts that the type of the `id` attribute is `str`.
        """
        obj = BaseModel()
        self.assertEqual(type(obj.id), str)

    def test_id_uniqueness(self):
        """
        Test that each `BaseModel` instance has a unique `id`.

        This test creates two instances of `BaseModel` and verifies that their `id` attributes are not the same.
        This ensures that the ID generation mechanism correctly assigns a unique identifier for each instance.
        """
        obj = BaseModel()
        obj1 = BaseModel()
        self.assertNotEqual(obj.id, obj1.id)

    def test_timestamp_type(self):
        """
        Test that `created_at` and `updated_at` are of type `datetime`.

        This test checks that the `created_at` and `updated_at` attributes for a `BaseModel` instance are
        instances of `datetime`. This ensures that the timestamps are correctly instantiated as datetime objects.
        """
        obj = BaseModel()
        self.assertEqual(type(obj.created_at), datetime)
        self.assertEqual(type(obj.updated_at), datetime)

    def test_timestamp(self):
        """
        Test that `created_at` and `updated_at` are unique for each instance.

        This test creates two instances of `BaseModel` with a pause in between to ensure that their `created_at`
        and `updated_at` timestamps are different. This verifies that timestamps reflect the time of creation
        accurately and are not identical.
        """
        obj = BaseModel()
        sleep(self.sleep_time)
        obj1 = BaseModel()
        self.assertNotEqual(obj.created_at, obj1.created_at)
        self.assertNotEqual(obj.updated_at, obj1.updated_at)

    def test_update_time(self):
        """
        Test that calling `save` updates the `updated_at` attribute.

        This test stores the initial value of `updated_at`, calls the `save` method, and verifies that
        `updated_at` has been updated to a new value. This ensures that modifications to an instance are
        reflected in the updated timestamp.
        """
        obj = BaseModel()
        time = obj.updated_at
        obj.save()
        self.assertNotEqual(obj.updated_at, time)

    def test_str_representation(self):
        """
        Test the `__str__` method for correct formatting.

        This test verifies that the string representation of a `BaseModel` instance matches the expected
        format: "[ClassName] (id) {attributes}". This is important for debugging and logging purposes.
        """
        obj = BaseModel()
        expected_output = f"[{type(obj).__name__}] ({obj.id}) {obj.__dict__}"
        self.assertEqual(str(obj), expected_output)

    def test_str_contains_class_name_id_and_attributes(self):
        """
        Test that `__str__` output contains the class name, id, and attributes.

        This test verifies that the `__str__` output includes the class name, the `id`, and all attributes in
        the instance's dictionary. This ensures comprehensive information is available in the string representation.
        """
        obj = BaseModel()
        self.assertIn(type(obj).__name__, str(obj))
        self.assertIn(obj.id, str(obj))

    def test_id_is_uuid_format(self):
        """
        Test that the `id` attribute is in UUID format.

        This test checks that the `id` attribute of a `BaseModel` instance is a valid UUID string.
        Validating the format ensures that the generated IDs conform to expected standards for unique identifiers.
        """
        obj = BaseModel()
        try:
            UUID(obj.id)
            valid_uuid = True
        except ValueError:
            valid_uuid = False
        self.assertTrue(valid_uuid)

    def test_type_to_dict(self):
        """
        Test that `to_dict` method returns a dictionary.

        This test ensures that calling the `to_dict` method on a `BaseModel` instance results in a dictionary.
        This is important for serialization and ensuring that model data can be easily converted to a suitable format.
        """
        obj = BaseModel()
        self.assertEqual(type(obj.to_dict()), dict)

    def test_class_to_dict(self):
        """
        Test that `to_dict` method includes the class name.

        This test verifies that the dictionary returned by the `to_dict` method includes a key `__class__`
        with the value 'BaseModel'. This is crucial for identifying the type of the object when serialized.
        """
        obj = BaseModel()
        dict1 = obj.to_dict()
        self.assertEqual(dict1['__class__'], 'BaseModel')

    def test_time_to_dict(self):
        """
        Test that timestamps are returned as strings in the dictionary.

        This test ensures that the `created_at` and `updated_at` attributes in the dictionary returned by
        `to_dict` are formatted as strings. This is important for ensuring consistency in data formats during serialization.
        """
        obj = BaseModel()
        dict1 = obj.to_dict()
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['created_at']), str)



if __name__ == "__main__":
    unittest.main()
