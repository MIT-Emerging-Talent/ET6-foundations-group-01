"""
Unit Test for Capitalize Character Function

This file tests the `capitalize_character` function, ensuring it behaves
as expected, including valid and invalid inputs.

Created on 12/28/2024

Author: Khadija Al Ramlawi
"""

import unittest
from solutions.capitalize_character import capitalize_character


class TestCapitalizeCharacter(unittest.TestCase):
    """
    Test cases to validate the functionality of the capitalize_character function.
    """

    def test_single_occurrence(self):
        """Test capitalizing a single occurrence of a character."""
        self.assertEqual(capitalize_character("hello", "h"), "Hello")

    def test_multiple_occurrences(self):
        """Test capitalizing multiple occurrences of a character."""
        self.assertEqual(capitalize_character("hello", "l"), "heLLo")

    def test_no_occurrence(self):
        """Test with a character that does not exist in the word."""
        self.assertEqual(capitalize_character("hello", "z"), "hello")

    def test_empty_word(self):
        """Test with an empty string as the input word."""
        self.assertEqual(capitalize_character("", "a"), "")

    def test_single_character_word(self):
        """Test with a single-character word that matches the input character."""
        self.assertEqual(capitalize_character("a", "a"), "A")

    def test_special_characters(self):
        """Test capitalizing a special character in the string."""
        self.assertEqual(capitalize_character("he!lo!", "!"), "he!lo!")

    def test_numerical_characters(self):
        """Test capitalizing numerical characters in the string."""
        self.assertEqual(capitalize_character("h3ll0", "l"), "h3LL0")

    def test_invalid_input_word(self):
        """Test handling invalid input where the word is not a string."""
        with self.assertRaises(AssertionError):
            capitalize_character(123, "a")

    def test_invalid_input_char(self):
        """Test handling invalid input where the character is not a string."""
        with self.assertRaises(AssertionError):
            capitalize_character("hello", 123)

    def test_multiple_characters_as_input(self):
        """Test handling input where the character parameter has multiple characters."""
        with self.assertRaises(AssertionError):
            capitalize_character("hello", "ll")
