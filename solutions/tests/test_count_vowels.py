#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Unit tests for the count_vowels function.

Created on 2024-12-27

@author: Yuri Spizhovyi
"""

import unittest
from solutions.count_vowels import count_vowels


class TestCountVowels(unittest.TestCase):
    """
    This class contains unit tests for the count_vowels function.
    The function takes a string and counts vowels.
    """

    def test_zero_text(self):
        """It should be zero empty string"""
        self.assertEqual(count_vowels(""), 0)

    def test_zero_occurrence(self):
        """It should be zero vowel in a string"""
        self.assertEqual(count_vowels("0"), 0)

    def test_single_occurrence(self):
        """It should be a one vowel in a string"""
        self.assertEqual(count_vowels("what"), 1)

    def test_multiple_occurrence(self):
        """It should be two vowels in a string"""
        self.assertEqual(count_vowels("Hello"), 2)

    def test_case_insensitive(self):
        """It should take into account upper and lowercase vowels"""
        self.assertEqual(count_vowels("Austria"), 4)

    def test_multiple_words(self):
        """It should count vowels of entire string"""
        self.assertEqual(count_vowels("Hello, World!"), 3)

    def test_non_string_item(self):
        """It should raise TypeError with a specific message
        when the input is not a string"""
        with self.assertRaises(AssertionError) as context:
            count_vowels(1)
        self.assertEqual(str(context.exception), "Input should be a string")


if __name__ == "__main__":
    unittest.main()
