#!/usr/bin/python3
""" Unittest for Amenity class """
from tests.test_models.test_base_model import test_basemodel
from models.amenity import Amenity
import pycodestyle


class test_Amenity(test_basemodel):
    """ Test cases for Amenity class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "Amenity"
        self.value = Amenity

    def test_name2(self):
        """ Test for name type """
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_pep8(self):
        """ Test for pycodestyle """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/amenity.py"])
        self.assertEqual(result.total_errors, 0, "pycodestyle failed")

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(Amenity.__doc__)
