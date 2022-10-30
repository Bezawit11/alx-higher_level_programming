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
        
if __name__ == '__main__':
    unittest.main()
