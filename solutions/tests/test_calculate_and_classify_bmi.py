#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
UnitTest module for BMI calculate and classify function.

Test categories:
 - Standard cases: typical weight and height inputs with various BMI ranges
 - Edge cases: edge cases for weight and height, including;
   negative values, zero values, and extremely large or small numbers
 - Defensive tests: wrong or invalid input types, assertions, etc.

Created on 2024-12-30
Author: Olumide Kolawole
"""

import unittest
from ..calculate_and_classify_bmi import calculate_and_classify_bmi


class TestCalculateAndClassifyBmi(unittest.TestCase):
    """Unit tests for the calculate_and_classify_bmi function."""

    # Standard test cases
    def test_normal_bmi(self):
        """It should classify BMI as 'Normal' and calculate 22.9."""
        self.assertAlmostEqual(calculate_and_classify_bmi(70, 1.75), ("Normal", 22.9))

    def test_underweight_bmi(self):
        """It should classify BMI as 'Underweight' and calculate 15.4."""
        self.assertAlmostEqual(
            calculate_and_classify_bmi(50, 1.80), ("Underweight", 15.4)
        )

    def test_overweight_bmi(self):
        """It should classify BMI as 'Overweight' and calculate 27.8."""
        self.assertAlmostEqual(
            calculate_and_classify_bmi(85, 1.75), ("Overweight", 27.8)
        )

    def test_obese_bmi(self):
        """It should classify BMI as 'Obese' and calculate 46.9."""
        self.assertAlmostEqual(calculate_and_classify_bmi(120, 1.6), ("Obese", 46.9))

    # Edge Cases
    def test_zero_weight_raises_valueerror(self):
        """It should raise a ValueError for zero weight."""
        with self.assertRaises(ValueError):
            calculate_and_classify_bmi(0, 1.75)

    def test_zero_height_raises_valueerror(self):
        """It should raise a ValueError for zero height."""
        with self.assertRaises(ValueError):
            calculate_and_classify_bmi(70, 0)

    def test_negative_weight_raises_valueerror(self):
        """It should raise a ValueError for negative weight."""
        with self.assertRaises(ValueError):
            calculate_and_classify_bmi(-70, 1.75)

    def test_negative_height_raises_valueerror(self):
        """It should raise a ValueError for negative height."""
        with self.assertRaises(ValueError):
            calculate_and_classify_bmi(70, -1.75)

    # Defensive tests
    def test_string_weight_raises_typeerror(self):
        """It should raise a AssertionError for string weight."""
        with self.assertRaises(AssertionError):
            calculate_and_classify_bmi("70", 1.75)

    def test_string_height_raises_typeerror(self):
        """It should raise a AssertionError for string height."""
        with self.assertRaises(AssertionError):
            calculate_and_classify_bmi(70, "1.75")

    def test_none_weight_raises_typeerror(self):
        """It should raise a AssertionError for None weight."""
        with self.assertRaises(AssertionError):
            calculate_and_classify_bmi(None, 1.75)

    def test_none_height_raises_typeerror(self):
        """It should raise a AssertionError for None height."""
        with self.assertRaises(AssertionError):
            calculate_and_classify_bmi(70, None)


if __name__ == "__main__":
    unittest.main()
