#!/usr/bin/python3
""" Unittest for User class """
from tests.test_models.test_base_model import test_basemodel
from models.user import User
import pycodestyle


class test_User(test_basemodel):
    """ Test cases for User class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "User"
        self.value = User

    def test_first_name(self):
        """ Test for first_name type """
        new = self.value()
        self.assertNotEqual(type(new.first_name), str)

    def test_last_name(self):
        """ Test for last_name type """
        new = self.value()
        self.assertNotEqual(type(new.last_name), str)

    def test_email(self):
        """ Test for email type """
        new = self.value()
        self.assertNotEqual(type(new.email), str)

    def test_password(self):
        """ Test for password type """
        new = self.value()
        self.assertNotEqual(type(new.password), str)

    def test_pep8(self):
        """ Test for pycodestyle """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/user.py"])
        self.assertEqual(result.total_errors, 0, "pycodestyle failed")

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(User.__doc__)
