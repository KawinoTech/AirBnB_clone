#!/usr/bin/python3
"""
Unit tests for the BaseModel class.

This module contains unit tests for the `BaseModel`
class, which defines the common attributes and methods for
other classes in a project.
The tests cover various aspects of the `BaseModel` class, including:
- Ensuring `id` uniqueness and validity
- Verifying timestamp types and updates
- Checking the string representation of the instance

Classes:
    TestBaseModel: Contains unit tests for the `BaseModel` class.

Attributes:
    sleep_time (int): Specifies the time in seconds to pause
    between tests that compare timestamps.
"""

import unittest
from models.base_model import BaseModel
from uuid import UUID
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class.

    This class contains tests for validating the functionality
    of the `BaseModel` class, such as unique ID generation,
    correct timestamp handling, and proper string representation format.

    Attributes:
        sleep_time (int): The time to sleep in seconds,
        used to ensure timestamps are different for certain tests.
    """

    sleep_time = 1

    def setUp(self) -> None:
        self.obj = BaseModel()

    def tearDown(self) -> None:
        pass

    def test_id(self):
        """
        Test that the `id` attribute is of type `str`.

        This test ensures that the `id` attribute generated
        for each instance of `BaseModel` is a string.
        The test creates an instance of `BaseModel` and asserts
        that the type of the `id` attribute is `str`.
        """
        obj = BaseModel()
        self.assertEqual(type(obj.id), str)

    def test_id_uniqueness(self):
        """
        Test that each `BaseModel` instance has a unique `id`.

        This test creates two instances of `BaseModel` and
        verifies that their `id` attributes are not the same.
        This ensures that the ID generation mechanism correctly
        assigns a unique identifier for each instance.
        """
        obj1 = BaseModel()
        self.assertNotEqual(self.obj.id, obj1.id)

    def test_timestamp_type(self):
        """
        Test that `created_at` and `updated_at` are of type `datetime`.

        This test checks that the `created_at` and `updated_at`
        attributes for a `BaseModel` instance are
        instances of `datetime`. This ensures that the timestamps are
        correctly instantiated as datetime objects.
        """
        self.assertEqual(type(self.obj.created_at), datetime)
        self.assertEqual(type(self.obj.updated_at), datetime)

    def test_timestamp(self):
        """
        Test that `created_at` and `updated_at` are unique for each instance.

        This test creates two instances of `BaseModel` with a
        pause in between to ensure that their `created_at`
        and `updated_at` timestamps are different. This verifies
        that timestamps reflect the time of creation
        accurately and are not identical.
        """
        sleep(self.sleep_time)
        obj1 = BaseModel()
        self.assertNotEqual(self.obj.created_at, obj1.created_at)
        self.assertNotEqual(self.obj.updated_at, obj1.updated_at)

    def test_update_time(self):
        """
        Test that calling `save` updates the `updated_at` attribute.

        This test stores the initial value of `updated_at`,
        calls the `save` method, and verifies that
        `updated_at` has been updated to a new value. This ensures
        that modifications to an instance are
        reflected in the updated timestamp.
        """
        time = self.obj.updated_at
        self.obj.save()
        self.assertNotEqual(self.obj.updated_at, time)

    def test_str_representation(self):
        """
        Test the `__str__` method for correct formatting.

        This test verifies that the string representation
        of a `BaseModel` instance matches the expected
        format: "[ClassName] (id) {attributes}". This is
        important for debugging and logging purposes.
        """
        expected_output = "[{}] ({}) {}".format(type(self.obj).__name__,
                                                self.obj.id,
                                                self.obj.__dict__)
        self.assertEqual(str(self.obj), expected_output)

    def test_str_contains_class_name_id_and_attributes(self):
        """
        Test that `__str__` output contains the class
        name, id, and attributes.

        This test verifies that the `__str__` output includes the
        class name, the `id`, and all attributes in
        the instance's dictionary. This ensures comprehensive information
        is available in the string representation.
        """
        self.assertIn(type(self.obj).__name__, str(self.obj))
        self.assertIn(self.obj.id, str(self.obj))

    def test_id_is_uuid_format(self):
        """
        Test that the `id` attribute is in UUID format.

        This test checks that the `id` attribute of a `BaseModel`
        instance is a valid UUID string.
        Validating the format ensures that the generated IDs conform
        to expected standards for unique identifiers.
        """
        try:
            UUID(self.obj.id)
            valid_uuid = True
        except ValueError:
            valid_uuid = False
        self.assertTrue(valid_uuid)

    def test_type_to_dict(self):
        """
        Test that `to_dict` method returns a dictionary.

        This test ensures that calling the `to_dict` method on a
        `BaseModel` instance results in a dictionary.
        This is important for serialization and ensuring that model
        data can be easily converted to a suitable format.
        """
        self.assertEqual(type(self.obj.to_dict()), dict)

    def test_class_to_dict(self):
        """
        Test that `to_dict` method includes the class name.

        This test verifies that the dictionary returned
        by the `to_dict` method includes a key `__class__`
        with the value 'BaseModel'. This is crucial for
        identifying the type of the object when serialized.
        """
        dict1 = self.obj.to_dict()
        self.assertEqual(dict1['__class__'], 'BaseModel')

    def test_time_to_dict(self):
        """
        Test that timestamps are returned as strings in the dictionary.

        This test ensures that the `created_at` and `updated_at`
        attributes in the dictionary returned by
        `to_dict` are formatted as strings. This is important for
        ensuring consistency in data formats during serialization.
        """
        dict1 = self.obj.to_dict()
        self.assertEqual(type(dict1['updated_at']), str)
        self.assertEqual(type(dict1['created_at']), str)

    def test_kwargs_type(self):
        """
        Test that `to_dict` method returns a dictionary type.

        This test checks that the result of calling `to_dict` on a `BaseModel`
        instance is a dictionary, ensuring that the
        method's output format is suitable
        for further processing or serialization.
        """
        self.assertEqual(type(self.obj.to_dict()), dict)

    def test_times_tamp(self):
        """
        Test that re-instantiating from
        dictionary format maintains timestamp types.

        This test initializes a new `BaseModel`
        instance using data from an existing
        instance's dictionary and confirms
        that `created_at` and `updated_at` remain
        as `datetime` objects, verifying that they are correctly deserialized.
        """
        new = BaseModel(self.obj.to_dict())
        self.assertEqual(type(new.created_at), datetime)
        self.assertEqual(type(new.updated_at), datetime)

    def test_kwargs_else_clause(self):
        """
        Test that `BaseModel` can be instantiated
        from a dictionary with matching attributes.

        This test initializes a new `BaseModel`
        instance using the dictionary representation
        of an existing instance and verifies that `id`,
        `created_at`, and `updated_at`
        attributes match those of the original instance.
        This ensures that the class
        handles dictionary-based instantiation accurately.
        """
        dict1 = self.obj.to_dict()
        new = BaseModel(**dict1)

        self.assertEqual(new.created_at, self.obj.created_at)
        self.assertEqual(new.updated_at, self.obj.updated_at)
        self.assertEqual(new.id, self.obj.id)

    def test_init_with_kwargs_only(self):
        """
        Test that initializing `BaseModel` with
        `kwargs` only correctly sets attributes.
        This test provides only keyword arguments to
        initialize a `BaseModel` instance,
        ensuring that each attribute in `kwargs` is correctly assigned.
        """
        data = {
            'id': '1234',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'name': 'TestModel'
        }
        obj = BaseModel(**data)
        self.assertEqual(obj.id, data['id'])
        self.assertEqual(obj.name, data['name'])

    def test_modify_attributes_and_save(self):
        """
        Test that modifying an attribute and
        calling `save()` updates `updated_at`.

        This test updates an instance attribute, calls `save()`, and verifies
        that `updated_at` reflects the modification time.
        """
        initial_updated_at = self.obj.updated_at
        self.obj.name = "NewName"
        self.obj.save()
        self.assertNotEqual(self.obj.updated_at, initial_updated_at)
        self.assertEqual(self.obj.name, "NewName")

    def test_to_dict_format_consistency(self):
        """
        Test that `to_dict()` returns a dictionary with correct keys and types.

        This test verifies that the dictionary produced
        by `to_dict()` includes all
        expected attributes and that the format of
        `created_at` and `updated_at`
        is a string in ISO format.
        """
        obj_dict = self.obj.to_dict()
        self.assertIn('id', obj_dict)
        self.assertIn('created_at', obj_dict)
        self.assertIn('updated_at', obj_dict)
        self.assertIn('__class__', obj_dict)
        self.assertEqual(type(obj_dict['created_at']), str)
        self.assertEqual(type(obj_dict['updated_at']), str)
        self.assertEqual(obj_dict['__class__'], 'BaseModel')

    def test_save_method_accuracy(self):
        """
        Test that calling `save()` only updates
        `updated_at` and not `created_at`.

        This test checks that `created_at` remains
        unchanged after calling `save()`
        while `updated_at` is updated to the current time.
        """
        initial_created_at = self.obj.created_at
        self.obj.save()
        self.assertEqual(self.obj.created_at, initial_created_at)
        self.assertNotEqual(self.obj.updated_at, initial_created_at)

    def test_create_instance_without_kwargs(self):
        """
        Test creating an instance of `BaseModel` without `kwargs`.

        This test verifies that an instance created without
        any arguments still initializes
        with default `id`, `created_at`, and `updated_at` attributes.
        """
        obj = BaseModel()
        self.assertIsInstance(obj.id, str)
        self.assertIsInstance(obj.created_at, datetime)
        self.assertIsInstance(obj.updated_at, datetime)


if __name__ == "__main__":
    unittest.main()
