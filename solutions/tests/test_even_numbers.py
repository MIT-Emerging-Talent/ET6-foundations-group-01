#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the even_numbers function.

Created on 2024-12-28

@author: Mykyta Kondratiev
"""

import unittest

from solutions.even_numbers import even_numbers


class TestAllEven(unittest.TestCase):
    """
    This class contains unit tests for the even_numbers function.
    The function checks if all numbers in a list are even.
    """

    def test_empty_list(self):
        """It should return True for an empty list"""
        self.assertTrue(even_numbers([]))

    def test_all_even(self):
        """It should return True if all numbers are even"""
        self.assertTrue(even_numbers([2, 4, 6, 8]))

    def test_one_odd(self):
        """It should return False if any number is odd"""
        self.assertFalse(even_numbers([2, 3, 6, 8]))

    def test_all_odd(self):
        """It should return False if all numbers are odd"""
        self.assertFalse(even_numbers([1, 3, 5]))

    def test_negative_numbers(self):
        """It should return True for all even negative numbers"""
        self.assertTrue(even_numbers([-2, -4, -6]))

    def test_zero(self):
        """It should return True for a list containing zero"""
        self.assertTrue(even_numbers([0]))

    def test_non_list_input(self):
        """It should raise AssertionError when the input is not a list"""
        with self.assertRaises(AssertionError) as context:
            even_numbers(123)
        self.assertEqual(str(context.exception), "Input should be a list")

    def test_none_input(self):
        """It should raise AssertionError when the input is None"""
        with self.assertRaises(AssertionError) as context:
            even_numbers(None)
        self.assertEqual(str(context.exception), "Input cannot be None")

    def test_non_integer_elements(self):
        """It should raise AssertionError if any element is not an integer"""
        with self.assertRaises(AssertionError) as context:
            even_numbers([2, "4", 6])
        self.assertEqual(
            str(context.exception), "All elements in the list must be integers"
        )
