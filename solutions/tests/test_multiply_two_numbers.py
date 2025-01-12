"""
Test module for multiply two numbers function.

Created 2025-01-04

@author: Manezhah Mohmand
"""

import unittest
from solutions.multiply_two_numbers import multiply_two_numbers


class TestMultiplyTwoNumbers(unittest.TestCase):
    """Tests for multiply_two_numbers function."""

    # Standard cases
    def test_two_positive_numbers(self):
        """It should return the product of two positive integers."""
        self.assertEqual(multiply_two_numbers(2, 3), 6)

    def test_two_negative_numbers(self):
        """It should return the product of two negative integers."""
        self.assertEqual(multiply_two_numbers(-2, -3), 6)

    def test_positive_and_negative_number(self):
        """It should return the product of a positive and a negative integer."""
        self.assertEqual(multiply_two_numbers(-2, 3), -6)

    # Boundary cases
    def test_zero_with_positive_number(self):
        """It should return 0 when one number is 0 and the other is positive."""
        self.assertEqual(multiply_two_numbers(0, 5), 0)

    def test_zero_with_negative_number(self):
        """It should return 0 when one number is 0 and the other is negative."""
        self.assertEqual(multiply_two_numbers(0, -7), 0)

    # Defensive tests
    def test_non_integer_input(self):
        """It should raise a TypeError when the inputs are not integers."""
        with self.assertRaises(TypeError):
            multiply_two_numbers(2.5, 3)

    def test_string_input(self):
        """It should raise a TypeError when one or both inputs are strings."""
        with self.assertRaises(TypeError):
            multiply_two_numbers("2", "3")


if __name__ == "__main__":
    unittest.main()
