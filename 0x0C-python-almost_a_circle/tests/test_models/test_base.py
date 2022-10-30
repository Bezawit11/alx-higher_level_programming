#!/usr/bin/python3

import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import sys
from io import StringIO
import pep8
import json
import os
    
class TestBase(unittest.TestCase):
    '''Tests the Base class.'''
    def test_nb_objects_private(self):
        """Tests if nb_objects is private class attribute"""
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
    
    def test_id(self):
        Base._Base__nb_objects = 0
        b1 = Base(3)
        b2 = Base(12)
        b3 = Base(4)
        self.assertEqual(b1.id, 3)
        self.assertEqual(b2.id, 12)
        self.assertEqual(b3.id, 4)
        
    def test_nb_objects_initialized(self):
        '''Tests if nb_objects initializes to zero.'''
        b = base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), 0)
     
    def test_id_count(self):
        """      """
        b = Base()
        self.assertEqual(getattr(Base, "_Base__nb_objects"), b.id)
        
    def test_JSON(self):
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(str(type(dictionary)), "<class 'dict'>")
        self.assertEqual(str(type(json_dictionary)), "<class 'str'>")
        
    def test_to_json_string(self):
        with self.assertRaises(TypeError) as e:
            Base.to_json_string()
        s = "to_json_string() missing 1 required positional argument: \
'list_dictionaries'"
        self.assertEqual(str(e.exception), s)
        self.assertEqual(Base.to_json_string(None), [])
        self.assertEqual(Base.to_json_string([]), "[]")
         
        a = [{'x': 2, 'y': 8, 'id': 1, 'height': 7, 'width': 10}]
        self.assertEqual(len(Base.to_json_string(a)), len(str(a)))
        a = [{}]
        self.assertEqual(Base.to_json_string(a), '[{}]')
         
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(1, 2, 3, 4)
        r3 = Rectangle(2, 3, 4, 5)
        dictionary = [r1.to_dictionary(), r2.to_dictionary(),
                      r3.to_dictionary()]
        json_dictionary = Base.to_json_string(dictionary)
        dictionary = str(dictionary)
        dictionary = dictionary.replace("'", '"')
        self.assertEqual(dictionary, json_dictionary)
         
if __name__ == '__main__':
    unittest.main()
