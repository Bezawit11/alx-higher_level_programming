#!/usr/bin/python3

import unittest
from models.base import Base
import sys
from io import StringIO
import pep8
import json
import os

class TestBase(unittest.TestCase):
    def test_id(self):
        Base._Base__nb_objects = 0
        b1 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 2)
    
    def test_rectangle(self):
        """Test check for rectangle
        """
        r1 = Rectangle(1, 2, 3)
        r1_dict = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dict)
        self.assertNotEqual(r1, r2)
    
    def test_square(self):
        """Test check for square creation
        """
        s1 = Square(10, 20, 30, 40)
        s1_dict = s1.to_dictionary()
        s2 = Rectangle.create(**s1_dict)
        self.assertNotEqual(s1, s2)
        
    

    def test_max_at_the_end(self):
        n = [1, 2, 3, 4]
        self.assertEqual(max_integer(n), 4)

    def test_string(self):
        o = [1, "2", 8, 3]
        with self.assertRaises(TypeError):
            max_integer(o)
    
    def test_empty(self):
        p = []
        self.assertIsNone(max_integer(p))
    
    def test_no_args(self):
        self.assertIsNone(max_integer())
    
    def test_morethan_1_args(self):
        a = [1, 2, 8, 3]
        b = [1, 2, 3]
        with self.assertRaises(TypeError):
            max_integer(a, b)
        
if __name__ == '__main__':
    unittest.main()
