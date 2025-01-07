"""
Test module for multiply two numbers function.

Created 2025-01-04

@author: Manezhah Mohmand
"""

import unittest
from solutions.multiply_two_numbers import multiply_two_numbers

class TestMultiplyTwoNumbers(unittest.TestCase):
    """Tests for multiply_two_numbers function."""

    def test_positive_numbers(self):
        """It should return the product of two positive numbers."""
        self.assertEqual(multiply_two_numbers(2, 3), 6)

    def test_negative_numbers(self):
        """It should return the product of two negative numbers."""
        self.assertEqual(multiply_two_numbers(-2, -3), 6)

    def test_mixed_sign_numbers(self):
        """It should return the product of one positive and one negative number."""
        self.assertEqual(multiply_two_numbers(-2, 3), -6)

if __name__ == "__main__":
    unittest.main()
