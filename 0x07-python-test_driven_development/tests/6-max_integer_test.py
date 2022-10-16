#!/usr/bin/python3

import unittest
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
        self.assertEqual(max_integer(p), None)
        
if __name__ == '__main__':
    unittest.main()
