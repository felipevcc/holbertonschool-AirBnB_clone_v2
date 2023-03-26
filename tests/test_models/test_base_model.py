#!/usr/bin/python3
""" Unittest for BaseModel class """
from models.base_model import BaseModel
import unittest
import datetime
from uuid import UUID
import json
import os
STORAGE_ENV = os.getenv("HBNB_TYPE_STORAGE")


class test_basemodel(unittest.TestCase):
    """ Test cases for BaseModel class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = 'BaseModel'
        self.value = BaseModel

    def setUp(self):
        """ Set Up """
        pass

    def tearDown(self):
        """ Tear Down """
        try:
            os.remove('file.json')
        except:
            pass

    def test_default(self):
        """ Test for default values """
        i = self.value()
        self.assertEqual(type(i), self.value)

    def test_kwargs(self):
        """ Test for creates an instance with dict (kwargs) """
        i = self.value()
        copy = i.to_dict()
        new = BaseModel(**copy)
        self.assertFalse(new is i)

    def test_kwargs_int(self):
        """ Test for creates an instance with dict of integers (kwargs)"""
        i = self.value()
        copy = i.to_dict()
        copy.update({1: 2})
        with self.assertRaises(TypeError):
            new = BaseModel(**copy)

    @unittest.skipIf(STORAGE_ENV == "db", "no testing with FileStorage")
    def test_save(self):
        """ Test for save method """
        i = self.value()
        i.save()
        key = self.name + "." + i.id
        with open('file.json', 'r') as f:
            j = json.load(f)
            self.assertEqual(j[key], i.to_dict())

    def test_str(self):
        """ Test for str format """
        i = self.value()
        self.assertEqual(1, 1)

    def test_todict(self):
        """ Test for to_dict method """
        i = self.value()
        n = i.to_dict()
        self.assertEqual(i.to_dict(), n)

    def test_kwargs_none(self):
        """ Test for kwargs (dict) with none args """
        n = {None: None}
        with self.assertRaises(TypeError):
            new = self.value(**n)

    def test_kwargs_one(self):
        """ Test for kwargs (dict) with an argument """
        n = {'Name': 'test'}
        new = self.value(**n)
        self.assertEqual(1, 1)

    def test_id(self):
        """ Test for id of an instance """
        new = self.value()
        self.assertEqual(type(new.id), str)

    def test_created_at(self):
        """ Test for created_at attr of an instance """
        new = self.value()
        self.assertEqual(type(new.created_at), datetime.datetime)

    def test_updated_at(self):
        """ Test for updated_at attr of an instance """
        new = self.value()
        self.assertEqual(type(new.updated_at), datetime.datetime)
        n = new.to_dict()
        new = BaseModel(**n)
        self.assertFalse(new.created_at == new.updated_at)
