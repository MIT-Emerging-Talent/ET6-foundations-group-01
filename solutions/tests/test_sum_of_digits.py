#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for sum_of_digits function.

Test Categories:
Standard Cases:

- Tests the function with typical, valid input values.
- Includes single-digit and multi-digit numbers.

Edge Cases:

- Tests boundary conditions and special cases.
- Includes zero, the largest single-digit number, and very large numbers.

Defensive Tests:

- Tests the function's response to invalid or unexpected inputs.
- Includes negative numbers and non-integer inputs.

Created on 2024-12-31
Author: Yurii Spizhovyi
"""

import unittest

from solutions.sum_of_digits import sum_of_digits


class TestSumOfDigits(unittest.TestCase):
    """Test suite for the sum_of_digits function."""

    def test_single_digit(self):
        """Test with a single-digit number."""
        self.assertEqual(sum_of_digits(5), 5)

    def test_multiple_digits(self):
        """Test with a multi-digit number."""
        self.assertEqual(sum_of_digits(1234), 10)

    def test_large_number(self):
        """Test with a large number."""
        self.assertEqual(sum_of_digits(987654321), 45)

    def test_zero(self):
        """Test with zero as input."""
        self.assertEqual(sum_of_digits(0), 0)

    def test_negative_number(self):
        """Test with a negative number (should raise ValueError)."""
        with self.assertRaises(ValueError):
            sum_of_digits(-123)

    def test_boundary_case(self):
        """Test with a boundary case of a large single-digit number."""
        self.assertEqual(sum_of_digits(9), 9)

    def test_non_integer_input(self):
        """Test with a non-integer input (should raise TypeError)."""
        with self.assertRaises(TypeError):
            sum_of_digits("1234")
        with self.assertRaises(TypeError):
            sum_of_digits(12.34)

    def test_negative_input(self):
        """Test with a negative integer input (should raise ValueError)."""
        with self.assertRaises(ValueError):
            sum_of_digits(-123)
