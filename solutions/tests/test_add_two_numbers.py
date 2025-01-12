"""
Test module for add two numbers function.

Test Categories:
Standard Cases:

- Tests the function with typical, valid input values.
- Includes positive and negative numbers.

Edge Cases:

- Tests boundary conditions and special cases.
- Includes zero, the largest single-digit number, and very large numbers.

Defensive Tests:

- Tests the function's response to invalid or unexpected inputs.

Created 2025-01-03

@author: Yurii Spizhovyi

"""

import unittest
from solutions.add_two_numbers import add_numbers


class TestAddTwoNumbers(unittest.TestCase):
    """The test for testing add_numbers function."""

    def test_positive_numbers(self):
        """It should be positive numbers"""
        self.assertEqual(add_numbers(2, 3), 5)

    def test_positive_negative_numbers(self):
        """It should be positive and negative numbers"""
        self.assertEqual(add_numbers(-1, 2), 1)

    def test_both_negative_numbers(self):
        """It should correctly add negative numbers"""
        self.assertEqual(add_numbers(-1, -2), -3)

    def test_large_numbers(self):
        """It should correctly add large numbers"""
        self.assertEqual(add_numbers(1000000, 2000000), 3000000)

    def test_zero_and_number(self):
        """It should correctly add zero and number"""
        self.assertEqual(add_numbers(0, 5), 5)

    def test_zeros_input(self):
        """It should return zero for both zeros in input"""
        self.assertEqual(add_numbers(0, 0), 0)

    def test_no_arguments(self):
        """It should raise an error when no argument are provided"""
        with self.assertRaises(TypeError):
            add_numbers()

    def test_float_input(self):
        with self.assertRaises(TypeError):
            add_numbers(1.25, 3)

    def test_non_integer_input(self):
        """It should raise TypeError for a non-integer input"""
        with self.assertRaises(TypeError):
            add_numbers("1", 2)

    def test_one_argument(self):
        """It should raise TypeError when only one argument is provided"""
        with self.assertRaises(TypeError):
            add_numbers(1)


if __name__ == "__main__":
    unittest.main()
