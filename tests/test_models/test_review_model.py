#!/usr/bin/python3
"""
Unit tests for the Review class.
"""

import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test cases for the Review class.
    """

    def setUp(self):
        """Set up a Review instance for each test method."""
        self.review = Review()

    def test_instance_creation(self):
        """
        Test that a Review instance is created successfully.
        Check that it is an instance of both Review and BaseModel.
        """
        self.assertIsInstance(self.review, Review)
        self.assertIsInstance(self.review, BaseModel)

    def test_default_attributes(self):
        """
        Test that all default attributes are correctly initialized.
        """
        self.assertEqual(self.review.place_id, "")
        self.assertEqual(self.review.user_id, "")
        self.assertEqual(self.review.text, "")

    def test_attribute_types(self):
        """
        Test that all attributes have the expected types.
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)

    def test_unique_id(self):
        """
        Test that each Review instance has a unique ID.
        """
        review2 = Review()
        self.assertNotEqual(self.review.id, review2.id)

    def test_text_assignment(self):
        """
        Test setting the text attribute on a Review instance.
        """
        self.review.text = "Great place to stay!"
        self.assertEqual(self.review.text, "Great place to stay!")

    def test_to_dict_contains_class(self):
        """
        Test that the dictionary representation of Review includes the '__class__' key.
        """
        review_dict = self.review.to_dict()
        self.assertIn("__class__", review_dict)
        self.assertEqual(review_dict["__class__"], "Review")

    def test_to_dict_format(self):
        """
        Test that the to_dict() method correctly formats attributes,
        including datetime fields in ISO format.
        """
        review_dict = self.review.to_dict()
        self.assertEqual(review_dict["text"], "")
        self.assertIn("created_at", review_dict)
        self.assertIn("updated_at", review_dict)
        # Check datetime format
        self.assertRegex(review_dict["created_at"], r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+")
        self.assertRegex(review_dict["updated_at"], r"\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d+")

    def test_str_representation(self):
        """
        Test the string representation of the Review instance.
        It should follow the format: [ClassName] (id) {attributes}.
        """
        expected_str = f"[Review] ({self.review.id}) {self.review.__dict__}"
        self.assertEqual(str(self.review), expected_str)

    def test_save_updates_updated_at(self):
        """
        Test that calling save() updates the updated_at attribute.
        """
        old_updated_at = self.review.updated_at
        self.review.save()
        self.assertNotEqual(self.review.updated_at, old_updated_at)
        self.assertGreater(self.review.updated_at, old_updated_at)


if __name__ == "__main__":
    unittest.main()
