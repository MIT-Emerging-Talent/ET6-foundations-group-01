#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for weight conversion function
Specifically for kilograms to pounds

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
from solutions.weight_conversion import kilograms_to_pounds


class TestWeightConversion(unittest.TestCase):
    """Testing kilogram to pound conversion function"""

    # Standard test cases
    def test_base_case_of_zero(self):
        """Test conversion of 0 kilograms"""
        self.assertEqual(kilograms_to_pounds(0), 0.0)

    def test_low_integer_value(self):
        """Test conversion of a low integer"""
        self.assertEqual(kilograms_to_pounds(1), 2.205)

    def test_higher_integer_value(self):
        """Test conversion of a high integer"""
        self.assertEqual(kilograms_to_pounds(200000000), 440924000.0)

    def test_low_float_number(self):
        """Test conversion of a low float number"""
        self.assertEqual(kilograms_to_pounds(2.205), 4.861)

    def test_higher_float_number(self):
        """Test conversion of a higher float value (144445.0992)"""
        self.assertEqual(kilograms_to_pounds(144445.0992), 318446.555)

    # Edge Cases

    def test_negative_integer(self):
        """Test conversion of a negative integer"""
        self.assertEqual(kilograms_to_pounds(-1), -2.205)

    def test_negative_float_number(self):
        """Test conversion of a negative float number"""
        self.assertEqual(kilograms_to_pounds(-2.205), -4.861)

    def test_extremely_large_number(self):
        """Test conversion of an extremely large number"""
        self.assertEqual(kilograms_to_pounds(100000000), 220462000.0)

    def test_extremely_small_number(self):
        """Test conversion of an extremely small number"""
        self.assertAlmostEqual(kilograms_to_pounds(0.000000001), 0.0)

    def test_exponential_number_for_kilograms_to_pounds(self):
        """Test converting exponential numbers for kilograms to pounds"""
        self.assertEqual(kilograms_to_pounds(1e-10), 0.000)  # 0.00002205

    # Defensive tests

    def test_input_string(self):
        """It should raise AssertionError for string inputs"""
        with self.assertRaises(AssertionError):
            kilograms_to_pounds("Thirty")

    def test_none_input(self):
        """It should raise AssertionError for None inputs"""
        with self.assertRaises(AssertionError):
            kilograms_to_pounds(None)

    def test_list_of_numbers(self):
        """It should raise AssertionError for list of numbers"""
        with self.assertRaises(AssertionError):
            kilograms_to_pounds([1, 2, 3])


if __name__ == "__main__":
    unittest.main()
