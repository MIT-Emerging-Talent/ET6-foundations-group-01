#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test module for `days_passed_2025` function.

Test Categories:
Standard Cases:
    - Tests the function with valid input dates within 2025.
    - Includes start of the year, mid-year, and end of the year dates.
Defensive Tests:
    - Tests the function's response to invalid or unexpected inputs.
    - Includes dates outside 2025 and non-date inputs.
Created on 2024-12-25
@author:Alemayehu Desta
"""

import unittest
from datetime import datetime

from solutions.days_passed_2025 import days_passed_2025


class TestDaysPassed2025(unittest.TestCase):
    """Unit tests for the time_elapsed_2025 function."""

    def test_days_at_start_of_year(self):
        """Test the calculation at the very start of 2025."""
        test_date = datetime(2025, 1, 1, 0, 0, 0)
        self.assertEqual(days_passed_2025(test_date), 1)

    def test_days_after_one_week(self):
        """Test the calculation after one week into 2025."""
        test_date = datetime(2025, 1, 8, 0, 0, 0)
        self.assertEqual(days_passed_2025(test_date), 8)

    def test_days_mid_year(self):
        """Test the calculation in the middle of the year 2025."""
        test_date = datetime(2025, 6, 30, 12, 0, 0)
        self.assertEqual(days_passed_2025(test_date), 181)

    def test_days_end_of_june(self):
        """Test the calculation at the end of June 2025."""
        test_date = datetime(2025, 6, 30, 23, 59, 59)
        self.assertEqual(days_passed_2025(test_date), 181)

    def test_days_end_of_year(self):
        """Test the calculation at the very end of 2025."""
        test_date = datetime(2025, 12, 31, 23, 59, 59)
        self.assertEqual(days_passed_2025(test_date), 365)

    def test_error_outside_2025(self):
        """Test that the function raises a ValueError outside the year 2025."""
        test_date = datetime(2024, 12, 31, 23, 59, 59)
        with self.assertRaises(ValueError):
            days_passed_2025(test_date)

    def test_error_non_date_input(self):
        """Test that the function raises a TypeError for non-date inputs."""
        non_date_inputs = [
            "2025-01-01",
            20250101,
            None,
            3.14,
            [2025, 1, 1],
            {"year": 2025, "month": 1, "day": 1},
        ]
        self._assert_raises_type_error_for_invalid_input(non_date_inputs)

    def _assert_raises_type_error_for_invalid_input(self, inputs):
        """Helper function to assert that the function raises TypeError for invalid inputs."""
        for input_value in inputs:
            with self.assertRaises(TypeError):
                days_passed_2025(input_value)


if __name__ == "__main__":
    unittest.main()
