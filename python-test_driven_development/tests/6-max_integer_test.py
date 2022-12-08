#!/usr/bin/python3
"""Unittest for max_integer([..])"""


import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """Unittests for the function max_integer"""

    def test_empty_list(self):
        empty = []
        self.assertEqual(max_integer(empty), None)

    def test_one_integer_list(self):
        one_element = [1]
        self.assertEqual(max_integer(one_element), 1)

    def test_sorted_list(self):
        ordered = [32, 64, 128, 256]
        self.assertEqual(max_integer(ordered), 256)

    def test_reverse_sorted_intiger_list(self):
        ordered = [1024, 512, 256, 128, 64]
        self.assertEqual(max_integer(ordered), 1024)

    def test_random_integer list(self):
        ordered = [98, -1024, 1, -21, 2795]
        self.assertEqual(max_integer(ordered), 2795)

    def test_negative_integer_list(self):
        ordered = [-35, -1024, -1, -21]
        self.assertEqual(max_integer(ordered), -1)

if __name__ == '__main__':
    unittest.main()
