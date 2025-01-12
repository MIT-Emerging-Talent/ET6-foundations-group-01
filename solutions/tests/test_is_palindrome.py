#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the is_palindrome function.
Created on 2025-01-03
@author: Mykyta Kondratiev
"""

import unittest

from solutions.is_palindrome import is_palindrome


class TestPalindrome(unittest.TestCase):
    """
    This class contains unit tests for the is_palindrome function.
    The function checks if a string is a palindrome.
    """

    def test_empty_string(self):
        """It should return True for an empty string"""
        self.assertTrue(is_palindrome(""))

    def test_simple_palindrome(self):
        """It should return True for a simple palindrome"""
        self.assertTrue(is_palindrome("racecar"))

    def test_simple_non_palindrome(self):
        """It should return False for a non-palindrome"""
        self.assertFalse(is_palindrome("hello"))

    def test_case_insensitive_palindrome(self):
        """It should return True for a palindrome with mixed case"""
        self.assertTrue(is_palindrome("RaceCar"))

    def test_palindrome_with_spaces_and_punctuation(self):
        """It should return True for palindromes with spaces and punctuation"""
        self.assertTrue(is_palindrome("A man a plan a canal Panama"))

    def test_non_alphanumeric_characters(self):
        """It should ignore non-alphanumeric characters"""
        self.assertTrue(is_palindrome("Was it a car or a cat I saw?"))

    def test_none_input(self):
        """It should raise AssertionError when the input is None"""
        with self.assertRaises(AssertionError) as context:
            is_palindrome(None)
        self.assertEqual(str(context.exception), "Input cannot be None")

    def test_non_string_input(self):
        """It should raise AssertionError when the input is not a string"""
        with self.assertRaises(AssertionError) as context:
            is_palindrome(12345)
        self.assertEqual(str(context.exception), "Input should be a string")

    def test_no_argument(self):
        """It should return True when no argument is given (default empty string)"""
        self.assertTrue(is_palindrome())
