#!/usr/bin/python3
'''Module for Square unit tests.'''
import unittest
from models.base import Base
from models.square import Square
from random import randrange
from contextlib import redirect_stdout
import io


class TestSquare(unittest.TestCase):
    '''Tests the Base class.'''

    def setUp(self):
        '''Imports module, instantiates class'''
        Base._Base__nb_objects = 0

    def tearDown(self):
        '''Cleans up after each test_method.'''
        pass

    # ----------------- Tests for #2 ------------------------

    def test_A_class(self):
        '''Tests Square class type.'''
        self.assertEqual(str(Square),
                         "<class 'models.square.Square'>")

    def test_B_inheritance(self):
        '''Tests if Square inherits Base.'''
        self.assertTrue(issubclass(Square, Base))

    def test_C_constructor_no_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square()
        s = "__init__() missing 1 required positional argument: 'size'"
        self.assertEqual(str(e.exception), s)

    def test_C_constructor_many_args(self):
        '''Tests constructor signature.'''
        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, 3, 4, 5)
        s = "__init__() takes from 2 to 5 positional arguments but 6 \
were given"
        self.assertEqual(str(e.exception), s)

    def test_D_instantiation(self):
        '''Tests instantiation.'''
        r = Square(10)
        self.assertEqual(str(type(r)), "<class 'models.square.Square'>")
        self.assertTrue(isinstance(r, Base))
        d = {'_Rectangle__height': 10, '_Rectangle__width': 10,
             '_Rectangle__x': 0, '_Rectangle__y': 0, 'id': 1}
        self.assertDictEqual(r.__dict__, d)

        with self.assertRaises(TypeError) as e:
            r = Square("1")
        msg = "width must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, "2")
        msg = "x must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(TypeError) as e:
            r = Square(1, 2, "3")
        msg = "y must be an integer"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(-1)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, -2)
        msg = "x must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(1, 2, -3)
        msg = "y must be >= 0"
        self.assertEqual(str(e.exception), msg)

        with self.assertRaises(ValueError) as e:
            r = Square(0)
        msg = "width must be > 0"
        self.assertEqual(str(e.exception), msg)

    def test_D_instantiation_positional(self):
        '''Tests positional instantiation.'''
        r = Square(5, 10, 15)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 1}
        self.assertEqual(r.__dict__, d)

        r = Square(5, 10, 15, 20)
        d = {'_Rectangle__height': 5, '_Rectangle__width': 5,
             '_Rectangle__x': 10, '_Rectangle__y': 15, 'id': 20}
        self.assertEqual(r.__dict__, d)

if __name__ == "__main__":
    unittest.main()
