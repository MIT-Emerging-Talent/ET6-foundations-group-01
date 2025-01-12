#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created 01-05-2025
@author: Mithchell Cenatus

This module contains unit tests for the calculate_average function.
"""

import unittest

from solutions.average_of_integers import calculate_average


class TestCalculateAverage(unittest.TestCase):
    """
    This class contains unit tests for the calculate_average function.
    """

    def test_valid_list(self):
        """Test with a valid list of integers."""
        self.assertEqual(calculate_average([1, 2, 3, 4, 5, 6]), 3.5)

    def test_negative_numbers(self):
        """Test with a list containing negative numbers."""
        self.assertEqual(calculate_average([-1, -2, -3, -4]), -2.5)

    def test_mixed_numbers(self):
        """Test with a list containing both positive and negative numbers."""
        self.assertEqual(calculate_average([-3, 1, 2, 3]), 0.75)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertIsNone(calculate_average([]))

    def test_non_list_input(self):
        """Test with an input that is not a list."""
        with self.assertRaises(TypeError):
            calculate_average("not a list")

    def test_non_integer_elements(self):
        """Test with a list containing non-integer elements."""
        with self.assertRaises(TypeError):
            calculate_average([1, 2, "three", 4])

    def test_large_numbers(self):
        """Test with a list of large numbers."""
        self.assertEqual(
            calculate_average([1_000_000, 2_000_000, 3_000_000]), 2_000_000
        )

    def test_single_element(self):
        """Test with a single element"""
        self.assertEqual(calculate_average([15]), 15.0)

    def test_all_zeros(self):
        """Test with a list containing all zeros."""
        self.assertEqual(calculate_average([0, 0, 0]), 0.0)


if __name__ == "__main__":
    unittest.main()
