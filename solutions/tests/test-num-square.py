#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for square number function

Test categories:
 - Standard cases: typical number input including both integers and floats.
 - Edge cases: edge cases for number input, including negative values, zero values.
 - Defensive tests: wrong or invalid input types, assertions, etc.

Created on 2025-01-07
Author : Manezhah "Mohmand"
"""

import unittest

from solutions.num_square import num_square

# Make sure this imports the square function correctly


class TestNumSquareFunction(unittest.TestCase):
    """Testing the square function"""

    def test_zero(self):
        """Test zero as input"""
        self.assertEqual(num_square(0), 0.0)

    def test_positive_integer(self):
        """Test positive integer input"""
        self.assertEqual(num_square(3), 9.0)

    def test_negative_integer(self):
        """Test negative integer input"""
        self.assertEqual(num_square(-4), 16.0)

    def test_positive_float(self):
        """Test positive float input"""
        self.assertEqual(num_square(2.5), 6.25)

    def test_negative_float(self):
        """Test negative float input"""
        self.assertEqual(num_square(-2.5), 6.25)

    def test_large_number(self):
        """Test a very large number"""
        self.assertEqual(num_square(100000), 10000000000.0)

    def test_input_string(self):
        """It should raise AssertionError for string inputs"""
        with self.assertRaises(AssertionError):
            num_square("five")

    def test_none_input(self):
        """It should raise AssertionError for None inputs"""
        with self.assertRaises(AssertionError):
            num_square(None)

    def test_list_input(self):
        """It should raise AssertionError for list inputs"""
        with self.assertRaises(AssertionError):
            num_square([1, 2, 3])

    def test_tuple_input(self):
        """It should raise AssertionError for tuple inputs"""
        with self.assertRaises(AssertionError):
            num_square((1, 2))


if __name__ == "__main__":
    unittest.main()
