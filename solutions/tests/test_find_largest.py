"""
Unit test for Find Largest Number Function

Created on 01/10/2025

Author : Khadija  Ramlawi
"""

import unittest
from solutions.find_largest import find_largest


class TestFindLargest(unittest.TestCase):
    def test_positive_numbers(self):
        # List with positive numbers
        self.assertEqual(find_largest([1, 2, 3]), 3)

    def test_mixed_numbers(self):
        # List with both positive and negative numbers
        self.assertEqual(find_largest([-10, 0, 5, 20]), 20)

    def test_all_negative_numbers(self):
        # List with all negative numbers
        self.assertEqual(find_largest([-5, -1, -10]), -1)

    def test_single_element(self):
        # List with a single element
        self.assertEqual(find_largest([42]), 42)

    def test_large_numbers(self):
        # List with large numbers
        self.assertEqual(find_largest([1000000, 5000000, 2000000]), 5000000)

    def test_empty_list(self):
        # Empty list should raise an AssertionError
        with self.assertRaises(AssertionError):
            find_largest([])

    def test_non_numeric_values(self):
        # List with non-numeric values should raise an AssertionError
        with self.assertRaises(AssertionError):
            find_largest([1, 2, "three"])

    def test_invalid_input_non_list(self):
        # Non-list input should raise an AssertionError
        with self.assertRaises(AssertionError):
            find_largest(123)

    def test_invalid_input_none(self):
        # None as input should raise an AssertionError
        with self.assertRaises(AssertionError):
            find_largest(None)
