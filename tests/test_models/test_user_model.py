#!/usr/bin/python3
"""
Unittest module for the User class.

This module contains test cases for the User class, which is a subclass
of BaseModel. It tests attribute initialization, inheritance from
BaseModel, and the default values of attributes specific to the User class.

Classes:
    TestUser: Contains test cases for the User class.
"""

import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for the User class.

    This class tests the initialization, default attribute values,
    and inheritance of the User class. It ensures the User class
    has the appropriate attributes with expected default values and
    correctly inherits functionality from BaseModel.
    """

    def setUp(self):
        """
        Sets up a new User instance for each test.
        """
        self.user = User()

    def test_is_instance_of_base_model(self):
        """
        Tests that User is an instance of BaseModel.
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_has_email_attribute(self):
        """
        Tests that the User class has an 'email' attribute with
        an initial empty string value.
        """
        self.assertTrue(hasattr(self.user, "email"))
        self.assertEqual(self.user.email, "")

    def test_has_password_attribute(self):
        """
        Tests that the User class has a 'password' attribute with
        an initial empty string value.
        """
        self.assertTrue(hasattr(self.user, "password"))
        self.assertEqual(self.user.password, "")

    def test_has_first_name_attribute(self):
        """
        Tests that the User class has a 'first_name' attribute with
        an initial empty string value.
        """
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertEqual(self.user.first_name, "")

    def test_has_last_name_attribute(self):
        """
        Tests that the User class has a 'last_name' attribute with
        an initial empty string value.
        """
        self.assertTrue(hasattr(self.user, "last_name"))
        self.assertEqual(self.user.last_name, "")

    def test_user_attribute_types(self):
        """
        Tests that User attributes are of type str.
        """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)

    def test_save_updates_updated_at(self):
        """
        Tests that calling save() updates the 'updated_at' attribute.
        """
        old_updated_at = self.user.updated_at
        self.user.save()
        self.assertNotEqual(self.user.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
