#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Test module for `emoji_sentiment` function.

Test Categories:
    - Tests the function with typical, valid input values.
    - Includes sentences with positive, negative, and neutral words.
    - Includes a test for case-insensitive matching of words.

created on 2025-12-29
@author: Alemayehu Desta
"""

import unittest
from solutions.emoji_sentiment import emoji_sentiment


class TestEmojiSentiment(unittest.TestCase):
    """
    Unit tests for the `emoji_sentiment` function. This class contains tests to verify
    the correct transformation of sentences into emojis based on sentiment.
    """

    def test_positive_sentence(self):
        """Test for a sentence with positive words."""
        result = emoji_sentiment("I am happy and sunny")
        self.assertEqual(result, "I am 🌞 and 🌞")

    def test_negative_sentence(self):
        """Test for a sentence with negative words."""
        result = emoji_sentiment("This is bad and rainy")
        self.assertEqual(result, "This is 🌧️ and 🌧️")

    def test_mixed_sentence(self):
        """Test for a sentence with both positive and negative words."""
        result = emoji_sentiment("I am happy but it is rainy")
        self.assertEqual(result, "I am 🌞 but it is 🌧️")

    def test_neutral_sentence(self):
        """Test for a sentence with neutral words."""
        result = emoji_sentiment("This is just a test")
        self.assertEqual(result, "This is just a test")

    def test_empty_input(self):
        """Test for an empty string input."""
        with self.assertRaises(ValueError):
            emoji_sentiment("")

    def test_non_string_input(self):
        """Test for non-string input."""
        with self.assertRaises(ValueError):
            emoji_sentiment(123)

    def test_single_word_positive(self):
        """Test for a single positive word."""
        result = emoji_sentiment("happy")
        self.assertEqual(result, "🌞")

    def test_single_word_negative(self):
        """Test for a single negative word."""
        result = emoji_sentiment("bad")
        self.assertEqual(result, "🌧️")

    def test_mixed_case_input(self):
        """Test for case-insensitive matching."""
        result = emoji_sentiment("I am Happy and SUNNY")
        self.assertEqual(result, "I am 🌞 and 🌞")


if __name__ == "__main__":
    unittest.main()
