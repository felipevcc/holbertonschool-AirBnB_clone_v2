#!/usr/bin/python3
""" Unittest for the console """
from console import HBNBCommand
import unittest
import sys
import io


class TestConsole(unittest.TestCase):
    """ Test cases for HBNBCommand class """

    def setUp(self):
        self.console = HBNBCommand()

    def test_create_instance(self):
        """ Test to review console output"""
        output = io.StringIO()
        sys.stdout = output
        self.console.onecmd('create State id="01234" name="California"')
        state_id = output.getvalue()
        sys.stdout = sys.__stdout__
        self.assertIn("01234", state_id)
