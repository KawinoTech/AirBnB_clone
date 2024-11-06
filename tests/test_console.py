#!/usr/bin/python3
"""Unit tests for the HBNBCommand class."""

import unittest
from io import StringIO
import sys
from models import storage
from models.base_model import BaseModel
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    """Unit tests for the HBNBCommand class commands."""

    def setUp(self):
        """Redirects stdout to capture CLI output for testing."""
        self.console = HBNBCommand()
        self.stdout = StringIO()
        sys.stdout = self.stdout
        storage.all().clear()  # Ensure clean state before each test

    def tearDown(self):
        """Restores stdout after test completion."""
        sys.stdout = sys.__stdout__

    def get_output(self):
        """Returns the output printed to stdout."""
        return self.stdout.getvalue().strip()

    def test_quit_command(self):
        """Test the 'quit' command to exit."""
        self.assertTrue(self.console.do_quit(None))

    def test_EOF_command(self):
        """Test the EOF (Ctrl+D) command to exit."""
        self.assertTrue(self.console.do_EOF(None))

    def test_emptyline(self):
        """Test that empty input doesn't raise errors."""
        self.console.emptyline()
        self.assertEqual(self.get_output(), "")

    def test_create_with_class_name(self):
        """Test 'create' command with valid class name."""
        self.console.onecmd("create BaseModel")
        output = self.get_output()
        self.assertTrue(len(output) > 0)  # Check if ID is printed
        self.assertIn("BaseModel." + output, storage.all())

    def test_create_without_class_name(self):
        """Test 'create' command without class name."""
        self.console.onecmd("create")
        self.assertEqual(self.get_output(), "** class name missing **")

    def test_create_with_invalid_class_name(self):
        """Test 'create' command with invalid class name."""
        self.console.onecmd("create MyModel")
        self.assertEqual(self.get_output(), "** class doesn't exist **")

    def test_show_with_class_name_and_id(self):
        """Test 'show' command with valid class name and ID."""
        instance = BaseModel()
        instance.save()
        self.console.onecmd(f"show BaseModel {instance.id}")
        self.assertIn(str(instance), self.get_output())

    def test_show_without_class_name(self):
        """Test 'show' command without class name."""
        self.console.onecmd("show")
        self.assertEqual(self.get_output(), "** class name missing **")

    def test_show_without_id(self):
        """Test 'show' command without ID."""
        self.console.onecmd("show BaseModel")
        self.assertEqual(self.get_output(), "** instance id missing **")

    def test_show_with_invalid_id(self):
        """Test 'show' command with an ID that doesn't exist."""
        self.console.onecmd("show BaseModel 12345")
        self.assertEqual(self.get_output(), "** no instance found **")

    def test_destroy_with_class_name_and_id(self):
        """Test 'destroy' command with valid class name and ID."""
        instance = BaseModel()
        instance.save()
        self.console.onecmd(f"destroy BaseModel {instance.id}")
        self.assertEqual(self.get_output(), "")
        self.assertNotIn("BaseModel." + instance.id, storage.all())

    def test_destroy_without_class_name(self):
        """Test 'destroy' command without class name."""
        self.console.onecmd("destroy")
        self.assertEqual(self.get_output(), "** class name missing **")

    def test_destroy_without_id(self):
        """Test 'destroy' command without ID."""
        self.console.onecmd("destroy BaseModel")
        self.assertEqual(self.get_output(), "** instance id missing **")

    def test_destroy_with_invalid_id(self):
        """Test 'destroy' command with an ID that doesn't exist."""
        self.console.onecmd("destroy BaseModel 12345")
        self.assertEqual(self.get_output(), "** no instance found **")

    def test_all_with_no_class_name(self):
        """Test 'all' command without specifying a class."""
        instance1 = BaseModel()
        instance1.save()
        instance2 = BaseModel()
        instance2.save()
        self.console.onecmd("all")
        output = self.get_output()
        self.assertIn(str(instance1), output)
        self.assertIn(str(instance2), output)

    def test_all_with_valid_class_name(self):
        """Test 'all' command with valid class name."""
        instance = BaseModel()
        instance.save()
        self.console.onecmd("all BaseModel")
        output = self.get_output()
        self.assertIn(str(instance), output)

    def test_all_with_invalid_class_name(self):
        """Test 'all' command with invalid class name."""
        self.console.onecmd("all MyModel")
        self.assertEqual(self.get_output(), "** class doesn't exist **")

    def test_update_with_class_id_attribute_value(self):
        """Test 'update' command with class name, ID, attribute, and value."""
        instance = BaseModel()
        instance.save()
        self.console.onecmd(f"update BaseModel {instance.id} name 'TestName'")
        self.console.onecmd(f"show BaseModel {instance.id}")
        self.assertIn("'name': 'TestName'", self.get_output())

    def test_update_without_class_name(self):
        """Test 'update' command without class name."""
        self.console.onecmd("update")
        self.assertEqual(self.get_output(), "** class name missing **")

    def test_update_without_id(self):
        """Test 'update' command without ID."""
        self.console.onecmd("update BaseModel")
        self.assertEqual(self.get_output(), "** instance id missing **")

    def test_update_without_attribute(self):
        """Test 'update' command without attribute name."""
        instance = BaseModel()
        instance.save()
        self.console.onecmd(f"update BaseModel {instance.id}")
        self.assertEqual(self.get_output(), "** attribute name missing **")

    def test_update_without_value(self):
        """Test 'update' command without attribute value."""
        instance = BaseModel()
        instance.save()
        self.console.onecmd(f"update BaseModel {instance.id} name")
        self.assertEqual(self.get_output(), "** value missing **")


if __name__ == "__main__":
    unittest.main()
