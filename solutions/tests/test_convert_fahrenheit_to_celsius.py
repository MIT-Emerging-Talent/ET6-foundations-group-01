#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the convert_fahrenheit_to_celsius function.

Created on 2024-12-29

@author: Yuri Spizhovyi
"""

import unittest
from solutions.convert_fahrenheit_to_celsius import convert_fahrenheit_to_celsius


class TestConvertFahrenheitToCelsius(unittest.TestCase):
    """Tests for the convert_fahrenheit_to_celsius function."""

    def test_freezing_point(self):
        """It should convert the freezing point of water (32°F) to 0°C."""
        self.assertEqual(convert_fahrenheit_to_celsius(32), 0.0)

    def test_boiling_point(self):
        """It should convert the boiling point of water (212°F) to 100°C."""
        self.assertEqual(convert_fahrenheit_to_celsius(212), 100.0)

    def test_negative_temperature(self):
        """It should correctly convert a negative Fahrenheit temperature."""
        self.assertEqual(convert_fahrenheit_to_celsius(-40), -40.0)

    def test_body_temperature(self):
        """It should correctly convert the average human body temperature."""
        self.assertEqual(convert_fahrenheit_to_celsius(98.6), 37.0)

    def test_decimal_input(self):
        """It should correctly handle decimal Fahrenheit values."""
        self.assertEqual(convert_fahrenheit_to_celsius(50.5), 10.3)

    def test_zero_fahrenheit(self):
        """It should convert 0°F to approximately -17.8°C."""
        self.assertEqual(convert_fahrenheit_to_celsius(0), -17.8)

    def test_non_number_input(self):
        """It should raise an assertion error for non-numeric input."""
        with self.assertRaises(AssertionError):
            convert_fahrenheit_to_celsius("thirty-two")

    def test_integer_as_string(self):
        """It should raise an assertion error for numeric input passed as a string."""
        with self.assertRaises(AssertionError):
            convert_fahrenheit_to_celsius("32")

    def test_empty_input(self):
        """It should raise an type error for an empty input passed"""
        with self.assertRaises(TypeError):
            convert_fahrenheit_to_celsius()


if __name__ == "__main__":
    unittest.main()
