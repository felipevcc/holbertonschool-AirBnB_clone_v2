#!/usr/bin/python3
""" Unittest for City class """
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import pycodestyle


class test_City(test_basemodel):
    """ Test cases for City class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    def test_state_id(self):
        """ Test for stated_id type """
        new = self.value()
        self.assertNotEqual(type(new.state_id), str)

    def test_name(self):
        """ Test for name type """
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_pep8(self):
        """ Test for pycodestyle """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/city.py"])
        self.assertEqual(result.total_errors, 0, "pycodestyle failed")

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(City.__doc__)
