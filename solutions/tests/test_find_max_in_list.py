#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the find_max_in_list function.

Created on 2024-12-27

@author: Yuri Spizhovyi
"""

import unittest
from solutions.find_max_in_list import find_max_in_list


class TestFindMaxInList(unittest.TestCase):
    """
    This class contains unit tests for the
    find_max_in_list function"""

    def test_empty_list(self):
        """It should be an empty list"""
        self.assertEqual(find_max_in_list([]), None)

    def test_zero_numbers(self):
        """It should be a zero numbers"""
        self.assertEqual(find_max_in_list([0, 0]), 0)

    def test_numbers(self):
        """It should be a list of integers"""
        self.assertEqual(find_max_in_list([1, 2, 3]), 3)

    def test_not_list(self):
        """It should be a string"""
        with self.assertRaises(TypeError) as context:
            find_max_in_list("not a list")
        self.assertEqual(str(context.exception), "Input must be a list of integers")

    def test_elements(self):
        """It should be a list of integers"""
        with self.assertRaises(TypeError) as context:
            find_max_in_list([1, "2", 3])
        self.assertEqual(
            str(context.exception), "All elements in the list must be integers"
        )


if __name__ == "__main__":
    unittest.main()
