#!/usr/bin/python3
""" Unittest for Place class """
from tests.test_models.test_base_model import test_basemodel
from models.place import Place
import pycodestyle


class test_Place(test_basemodel):
    """ Test cases for Place class """

    def __init__(self, *args, **kwargs):
        """ Init method """
        super().__init__(*args, **kwargs)
        self.name = "Place"
        self.value = Place

    def test_city_id(self):
        """ Test for city_id type """
        new = self.value()
        self.assertNotEqual(type(new.city_id), str)

    def test_user_id(self):
        """ Test for user_id type """
        new = self.value()
        self.assertNotEqual(type(new.user_id), str)

    def test_name(self):
        """ Test for name type """
        new = self.value()
        self.assertNotEqual(type(new.name), str)

    def test_description(self):
        """ Test for description type """
        new = self.value()
        self.assertNotEqual(type(new.description), str)

    def test_number_rooms(self):
        """ Test for number_rooms type """
        new = self.value()
        self.assertNotEqual(type(new.number_rooms), int)

    def test_number_bathrooms(self):
        """ Test for number_bathrooms type """
        new = self.value()
        self.assertNotEqual(type(new.number_bathrooms), int)

    def test_max_guest(self):
        """ Test for max_guest type """
        new = self.value()
        self.assertNotEqual(type(new.max_guest), int)

    def test_price_by_night(self):
        """ Test for price_by_night type """
        new = self.value()
        self.assertNotEqual(type(new.price_by_night), int)

    def test_latitude(self):
        """ Test for latitude type """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_longitude(self):
        """ Test for longitude type """
        new = self.value()
        self.assertNotEqual(type(new.latitude), float)

    def test_amenity_ids(self):
        """ Test for amenity_ids type """
        new = self.value()
        self.assertEqual(type(new.amenity_ids), list)

    def test_pep8(self):
        """ Test for pycodestyle """
        pep8style = pycodestyle.StyleGuide(quiet=True)
        result = pep8style.check_files(["models/place.py"])
        self.assertEqual(result.total_errors, 0, "pycodestyle failed")

    def test_docs(self):
        """ Test for doc """
        self.assertIsNotNone(Place.__doc__)
