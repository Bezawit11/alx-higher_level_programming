#!/usr/bin/python3

import unittest
class TestMaxInteger(unittest.TestCase):
    def test_all_negative(self):
        l = [1, 2, 8, 3]
        self.assertEqual(max_integer(l), 8)
