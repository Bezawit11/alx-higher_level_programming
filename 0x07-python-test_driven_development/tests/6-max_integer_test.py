#!/usr/bin/python3

import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    def test_all_positive(self):
        l = [1, 2, 8, 3]
        self.assertEqual(max_integer(l), 8)
    
    def test_all_equal(self):
        m = [3, 3, 3, 3]
        self.assertEqual(max_integer(m), 3)
        
    def test_all_negative(self):
        n = [-2, -5, -7, -4]
        self.assertEqual(max_integer(n), -2)
        
    def test_string(self):
        o = [1, "2", 8, 3]
        with self.assertRaises(TypeError)
            max_integer(string)
            
    def test_empty(self):
        p = []
        self.assertIsNone(max_integer(p))
        
    def test_no_args(self):
        self.assertIsNone(max_integer())
        
    def test_morethan_1_args(self):
        a = [1, 2, 8, 3]
        b = [1, 2, 3]
        with self.assertRaises(TypeError)
            max_integer(a, b)
        
if __name__ == '__main__':
    unittest.main()
