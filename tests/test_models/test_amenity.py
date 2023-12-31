#!/usr/bin/python3
"""
Unittest for amenity.py
"""
import datetime
import unittest

from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    """Tests instances and methods from amenity class"""

    a = Amenity()

    def test_class_exists(self) -> None:
        """tests if class exists"""
        res = "<class 'models.amenity.Amenity'>"
        self.assertEqual(str(type(self.a)), res)

    def test_user_inheritance(self) -> None:
        """test if Amenity is a subclass of BaseModel"""
        self.assertIsInstance(self.a, Amenity)

    def test_has_attributes(self) -> None:
        """verify if attributes exist"""
        self.assertTrue(hasattr(self.a, 'name'))
        self.assertTrue(hasattr(self.a, 'id'))
        self.assertTrue(hasattr(self.a, 'created_at'))
        self.assertTrue(hasattr(self.a, 'updated_at'))

    def test_types(self) -> None:
        """tests if the type of the attribute is the correct one"""
        self.assertIsInstance(self.a.name, str)
        self.assertIsInstance(self.a.id, str)
        self.assertIsInstance(self.a.created_at, datetime.datetime)
        self.assertIsInstance(self.a.updated_at, datetime.datetime)


if __name__ == '__main__':
    unittest.main()
