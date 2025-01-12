#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Unit tests for the fizzbuzz function.

Test Categories:
Standard Cases:
    - Valid inputs where n is a positive integer.
Edge Cases:
    - Handles special inputs, including minimal input values and no replacements.
Defensive Tests:
    - The function raises a ValueError for invalid inputs, such as non-integer types or negative numbers.

Created on 2025-05-01
@author: Alemayehu Desta
"""

import unittest

from solutions.fizzbuzz import fizzbuzz


class TestFizzBuzz(unittest.TestCase):
    """
    Tests for the fizzbuzz function.
    """

    def test_fizzbuzz_basic_case(self):
        """
        Test the basic functionality of fizzbuzz with n=5.
        """
        self.assertEqual(fizzbuzz(5), ["1", "2", "Fizz", "4", "Buzz"])

    def test_fizzbuzz_multiple_of_three_and_five(self):
        """
        Test if multiples of both 3 and 5 are replaced by 'FizzBuzz'.
        """
        self.assertEqual(fizzbuzz(15)[14], "FizzBuzz")

    def test_fizzbuzz_no_fizzbuzz(self):
        """
        Test if no replacements occur when n=2.
        """
        self.assertEqual(fizzbuzz(2), ["1", "2"])

    def test_fizzbuzz_non_integer(self):
        """
        Test that a ValueError is raised for non-integer input.
        """
        with self.assertRaises(ValueError):
            fizzbuzz("10")

    def test_fizzbuzz_negative(self):
        """
        Test that a ValueError is raised for negative input.
        """
        with self.assertRaises(ValueError):
            fizzbuzz(-5)

    def test_fizzbuzz_zero(self):
        """
        Test that a ValueError is raised for n=0.
        """
        with self.assertRaises(ValueError):
            fizzbuzz(0)

    def test_fizzbuzz_boundary_case(self):
        """
        Test the boundary case where n=1.
        """
        self.assertEqual(fizzbuzz(1), ["1"])

    def test_fizzbuzz_large_input(self):
        """
        Test that fizzbuzz can handle large values of n, e.g., n=1000.
        """
        result = fizzbuzz(1000)
        self.assertEqual(
            len(result), 1000
        )  # Check if the length of the list is correct.

    def test_fizzbuzz_float_input(self):
        """
        Test that a ValueError is raised for float input.
        """
        with self.assertRaises(ValueError):
            fizzbuzz(3.5)


if __name__ == "__main__":
    unittest.main()
