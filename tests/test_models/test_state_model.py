#!/usr/bin/python3
"""
Unit tests for the State class.
"""

import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for the State class.
    """

    def setUp(self):
        """Set up test environment for each test method."""
        self.state = State()

    def test_instance_creation(self):
        """
        Test that a State instance is created successfully.
        Check that it is an instance of both State and BaseModel.
        """
        self.assertIsInstance(self.state, State)
        self.assertIsInstance(self.state, BaseModel)

    def test_default_name(self):
        """
        Test the default value of the name attribute.
        It should be an empty string by default.
        """
        self.assertEqual(self.state.name, "")

    def test_name_assignment(self):
        """
        Test setting the name attribute on a State instance.
        """
        self.state.name = "California"
        self.assertEqual(self.state.name, "California")

    def test_unique_id(self):
        """
        Test that each State instance has a unique ID.
        """
        state2 = State()
        self.assertNotEqual(self.state.id, state2.id)

    def test_to_dict_contains_class(self):
        """
        Test that the dictionary representation of State includes the '__class__' key.
        """
        state_dict = self.state.to_dict()
        self.assertIn("__class__", state_dict)
        self.assertEqual(state_dict["__class__"], "State")

    def test_str_representation(self):
        """
        Test the string representation of the State instance.
        It should follow the format: [ClassName] (id) {attributes}.
        """
        expected_str = f"[State] ({self.state.id}) {self.state.__dict__}"
        self.assertEqual(str(self.state), expected_str)

    def test_save_updates_updated_at(self):
        """
        Test that calling save() updates the updated_at attribute.
        """
        old_updated_at = self.state.updated_at
        self.state.save()
        self.assertNotEqual(self.state.updated_at, old_updated_at)
        self.assertGreater(self.state.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
