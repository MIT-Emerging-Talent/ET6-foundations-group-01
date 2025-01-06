#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the sum_odd_numbers function.

Created on 2025-01-03

@author: Sukhrob Muborakshoev
"""

import unittest

from solutions.sum_odd_numbers import sum_odd_numbers


class TestSumOddNumbers(unittest.TestCase):
    """
    This class contains unit tests for the sum_odd_numbers function.
    The function gets a list of integers as an input and returns the sum of odd numbers.
    """

    def test_valid_list(self):
        """It should return 25"""
        self.assertEqual(sum_odd_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9]), 25)

    def test_negative_valid_list(self):
        """It should return -138"""
        self.assertEqual(sum_odd_numbers([10, -7, 3, 4, -51, 6, 7, -99, 9]), -138)

    def test_large_numbers(self):
        """It should correctly return sum of large odd numbers"""
        self.assertEqual(
            sum_odd_numbers(
                [
                    10**10,
                    10**10 + 1,
                    -(10**10 + 2),
                    -(10**10 + 3),
                    10**15 + 4,
                    10**15 + 5,
                ]
            ),
            1000000000000003,
        )

    def test_only_odd_numbers(self):
        """It should return 133"""
        self.assertEqual(sum_odd_numbers([3, 11, 7, 21, 91]), 133)

    def test_only_even_numbers(self):
        """It should return 0"""
        self.assertEqual(sum_odd_numbers([22, 90, 54, 100]), 0)

    def test_empty_list(self):
        """It should return 0"""
        self.assertEqual(sum_odd_numbers([]), 0)

    def test_not_all_integers(self):
        """It should return None"""
        self.assertEqual(sum_odd_numbers([3, "2", 5, 90, 33]), None)

    def test_no_argument_provided(self):
        """Test that a TypeError is raised when no arguments are provided."""
        with self.assertRaises(TypeError) as context:
            sum_odd_numbers(None)
        self.assertEqual(
            str(context.exception),
            "The function requires a list of integers as an argument.",
        )

    def test_argument_is_str(self):
        """Raises a TypeError when the input is a string."""
        with self.assertRaises(TypeError) as context:
            sum_odd_numbers("not a list")
        self.assertEqual(str(context.exception), "Input must be a list of integers.")

    def test_argument_is_number(self):
        """Raises a TypeError when the input is a number."""
        with self.assertRaises(TypeError) as context:
            sum_odd_numbers(123)
        self.assertEqual(str(context.exception), "Input must be a list of integers.")
