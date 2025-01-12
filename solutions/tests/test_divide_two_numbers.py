#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for dividing two numbers function.

Created 2025-01-04

@author: Henry Ogoe
"""

import unittest
from solutions.divide_two_numbers import divide_numbers


class TestDivideTwoNumbers(unittest.TestCase):
    """The test for testing divide_numbers function."""

    def test_positive_numbers(self):
        """It should return positive number 2"""
        self.assertEqual(divide_numbers(6, 3), 2)

    def test_positive_negative_numbers(self):
        """It should divide negative numerator by positive denominator"""
        self.assertEqual(divide_numbers(-6, 2), -3)

    def test_both_negative_numbers(self):
        """It should correctly divide negative numbers"""
        self.assertEqual(divide_numbers(-8, -2), 4)

    def test_large_numbers(self):
        """It should correctly divide large numbers"""
        self.assertEqual(divide_numbers(2000000, 1000000), 2)

    def test_zero_and_number(self):
        """It should return zero if numerator is zero"""
        self.assertEqual(divide_numbers(0, 5), 0)

    def test_zero_denominator(self):
        """It should return Value error for zero in denominator(b)"""
        with self.assertRaises(ValueError):
            divide_numbers(46, 0)

    def test_no_arguments(self):
        """It should raise an error when no argument are provided"""
        with self.assertRaises(TypeError):
            divide_numbers()

    def test_float_input(self):
        """It should raise an error for float input"""
        with self.assertRaises(TypeError):
            divide_numbers(6.25, 3)

    def test_non_integer_input(self):
        """It should raise TypeError for a non-integer input"""
        with self.assertRaises(TypeError):
            divide_numbers("4", 2)

    def test_one_argument(self):
        """It should raise TypeError when only one argument is provided"""
        with self.assertRaises(TypeError):
            divide_numbers(2)


if __name__ == "__main__":
    unittest.main()
