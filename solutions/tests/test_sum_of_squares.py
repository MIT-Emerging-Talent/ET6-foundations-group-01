#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 01-11-2025
@author: Mithchell Cenatus

This class contains unit tests for the sum_of_square function.
The function gets a list of integers and/or floats as input and returns the sum of the squares of its elements.
"""

import unittest

from solutions.sum_of_squares import sum_of_square


class TestSumOfSquare(unittest.TestCase):
    """
    Unit tests for the sum_of_square function.
    """

    def test_valid_list(self):
        """It should return 55 for [1, 2, 3, 4, 5]."""
        self.assertEqual(sum_of_square([1, 2, 3, 4, 5]), 55)

    def test_negative_valid_list(self):
        """It should return 102 for [-1, -2, 4, 9]."""
        self.assertEqual(sum_of_square([-1, -2, 4, 9]), 102)

    def test_mixed_numbers(self):
        """It should return 234.09 for [-5.3, 9, -11, 2]."""
        self.assertAlmostEqual(sum_of_square([-5.3, 9, -11, 2]), 234.09, places=2)

    def test_empty_list(self):
        """It should return 0 for an empty list."""
        self.assertEqual(sum_of_square([]), 0)

    def test_non_list_input(self):
        """Test that a TypeError is raised when input is not a list."""
        with self.assertRaises(TypeError):
            sum_of_square("not a list")

    def test_invalid_elements(self):
        """Test that a TypeError is raised when list contains invalid elements."""
        with self.assertRaises(TypeError):
            sum_of_square([20, 25, -1, "8"])

    def test_large_numbers(self):
        """It should return 2_000_000_000_001 for [1_000_000, 1, 0, -1_000_000]."""
        self.assertEqual(
            sum_of_square([1_000_000, 1, 0, -1_000_000]), 2_000_000_000_001
        )


if __name__ == "__main__":
    unittest.main()
