#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for convert an hourly wage to its equivalent monthly and yearly salaries.

Created 2025-01-04

@author: Henry Ogoe
"""

import unittest
from solutions.convert_salary import convert_salary


class TestConvertSalary(unittest.TestCase):
    """The test for testing convert_salary function."""

    def test_standard_case(self):
        """It should normally proceed standard numbers"""
        self.assertEqual(convert_salary(16.5), (2857.8, 34320.0))

    def test_different_hourly_rate(self):
        """It should accept different common hourly rates"""
        self.assertEqual(convert_salary(25), (4330.0, 52000))

    def test_large_salary(self):
        """It should correctly proceed big salaries"""
        self.assertEqual(convert_salary(1000000), (173200000.0, 2080000000))

    def test_low_salary(self):
        """It should correctly proceed very low salaries for proper rounding"""
        self.assertEqual(convert_salary(0.1), (17.32, 208.0))

    def test_custom_hours(self):
        """It should be able to use different weekly hours"""
        self.assertEqual(convert_salary(16.5, 100), (7144.5, 85800.0))

    def test_negative_salary(self):
        """It should raise error on negative salary"""
        with self.assertRaises(AssertionError):
            convert_salary(-8)

    def test_invalid_type(self):
        """It should raise error on non float input"""
        with self.assertRaises(AssertionError):
            convert_salary("7")


if __name__ == "__main__":
    unittest.main()
