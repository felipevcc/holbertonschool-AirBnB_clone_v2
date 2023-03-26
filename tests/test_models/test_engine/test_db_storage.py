#!/usr/bin/python3
""" Module for testing DBStorage class """
import unittest
from models import storage
from models.engine.db_storage import DBStorage
import pycodestyle
from os import getenv
STORAGE_ENV = getenv("HBNB_TYPE_STORAGE")


@unittest.skipIf(STORAGE_ENV != "db", "no testing with db storage")
class TestDBStorage(unittest.TestCase):
    """ Test cases for DBStorage class """

    def setUp(self):
        """ Set up test environment """
        del_list = []
        for key in storage.all().keys():
            del_list.append(key)
        for key in del_list:
            storage._DBStorage__session.delete(storage.all()[key])
            storage._DBStorage__session.commit()

    def test_storage_instance(self):
        """ DBStorage instance created """
        self.assertEqual(type(storage), DBStorage)

    def test_all(self):
        """ Test case for 'all' method """
        self.assertEqual(type(storage.all()), dict)

    def test_empty_db(self):
        """ Initially empty database"""
        self.assertEqual(len(storage.all()), 0)

    def test_storage(self):
        """ Test if an object is store in the database """
        from models.state import State
        new = State(name="California")
        new.save()
        objId = new.to_dict()['id']
        self.assertIn(new.__class__.__name__ + '.' + objId,
                        storage.all(type(new)).keys())


class TestDBStoragePEP8(unittest.TestCase):
    """ Test cases for the doc and style of DBStorage class """

    def test_pep8(self):
        """ Test for pycodestyle """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/engine/db_storage.py"])
        self.assertEqual(result.total_errors, 0, "pycodestyle failed")

    def test_docs(self):
        """ Test for doc in DBStorage methods """
        self.assertIsNotNone(DBStorage.__doc__)
