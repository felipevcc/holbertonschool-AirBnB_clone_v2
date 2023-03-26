#!/usr/bin/python3
""" Unittest for State class """
from tests.test_models.test_base_model import test_basemodel
from models.state import State
import pycodestyle


class test_state(test_basemodel):
    """ Test cases for State class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ Test for name type """
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_pep8(self):
        """ Test for pycodestyle """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/state.py"])
        self.assertEqual(result.total_errors, 0, "pycodestyle failed")

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(State.__doc__)
