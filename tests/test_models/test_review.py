#!/usr/bin/python3
""" Unittest for Review class """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import pycodestyle


class test_review(test_basemodel):
    """ Test cases for Review class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    def test_place_id(self):
        """ Test for place_id type """
        new = self.value()
        self.assertNotEqual(type(new.place_id), str)

    def test_user_id(self):
        """ Test for user_id type """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_text(self):
        """ Test for text type """
        new = self.value()
        self.assertNotEqual(type(new.text), str)

    def test_pep8(self):
        """ Test for pycodestyle """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/review.py"])
        self.assertEqual(result.total_errors, 0, "pycodestyle failed")

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(Review.__doc__)
