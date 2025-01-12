#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for weight conversion function
Specifically from pounds to kilograms

Test categories:
 - Standard cases: typical weight input with different units
 - Edge cases: edge cases for weight input, including;
   negative values, zero values, and non-numeric values
 - Defensive tests: wrong or invalid input types, assertions, etc.
Created on 2024-12-30
Author: Olumide Kolawole
"""

import unittest

# Error is going to occur because of how we're currently importing modules
from ..weight_conversion import pounds_to_kilograms


class TestWeightConversion(unittest.TestCase):
    """Testing pound to kilograms conversion function"""

    # Standard test cases
    def test_a_base_case_of_zero(self):
        """Test conversion of 0 pounds"""
        self.assertEqual(pounds_to_kilograms(0), 0.0)

    def test_low_integer_value(self):
        """Test conversion of a low integer"""
        self.assertEqual(pounds_to_kilograms(1), 0.454)

    def test_high_integer_value(self):
        """Test conversion of a high integer"""
        self.assertEqual(pounds_to_kilograms(5000), 2267.96)

    def test_low_float_number(self):
        """Test a low value float number"""
        self.assertEqual(pounds_to_kilograms(4.861), 2.205)

    def test_high_value_float_number(self):
        """Test a high value float number"""
        self.assertEqual(pounds_to_kilograms(317000.668), 143788.967)

    # Edge Cases

    def test_a_negative_integer_value(self):
        """Test conversion of a negative integer"""
        self.assertEqual(pounds_to_kilograms(-2), -0.907)

    def test_negative_float_number(self):
        """Test conversion of a negative float number"""
        self.assertEqual(pounds_to_kilograms(-4.861), -2.205)

    def test_extremely_large_number(self):
        """Test conversion of an extremely large number"""
        self.assertEqual(pounds_to_kilograms(220462000.0), 99999799.504)

    def test_extremely_small_number(self):
        """Test extremely small number"""
        self.assertEqual(pounds_to_kilograms(0.00002205), 0.0)

    # Defensive tests

    def test_input_string(self):
        """It should raise AssertionError for string inputs"""
        with self.assertRaises(AssertionError):
            pounds_to_kilograms("Thirty")

    def test_none_input(self):
        """It should raise AssertionError for None inputs"""
        with self.assertRaises(AssertionError):
            pounds_to_kilograms(None)

    def test_list_of_numbers(self):
        """It should raise AssertionError for list of numbers"""
        with self.assertRaises(AssertionError):
            pounds_to_kilograms([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
