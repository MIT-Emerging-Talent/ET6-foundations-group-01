#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created : 01-10-2025
@author : Mithchell Lawensky Cenatus

Test module for the sort_my_words function that asks the user to provide a list of words
and returns the words sorted in alphabetical order, placing special characters before regular words.

"""

import unittest

from solutions.sort_words import sort_my_words


class TestSortWords(unittest.TestCase):
    def test_valid_list(self):
        """Test sorting a valid list of strings."""
        input_data = ["banana", "apple", "cherry"]
        expected = ["apple", "banana", "cherry"]
        self.assertEqual(sort_my_words(input_data), expected)

    def test_empty_list(self):
        """Test sorting an empty list."""
        input_data = []
        expected = []
        self.assertEqual(sort_my_words(input_data), expected)

    def test_single_element_list(self):
        """Test sorting a list with a single element."""
        input_data = ["apple"]
        expected = ["apple"]
        self.assertEqual(sort_my_words(input_data), expected)

    def test_non_list_input(self):
        """Test handling non-list inputs."""
        with self.assertRaises(TypeError):
            sort_my_words("not a list")  # Non-list input

    def test_list_with_non_string_elements(self):
        """Test handling a list with non-string elements."""
        input_data = ["apple", 42, "banana"]  # 42 is not a string
        with self.assertRaises(TypeError):
            sort_my_words(
                input_data
            )  # List with non-string elements should raise TypeError

    def test_list_with_mixed_case_strings(self):
        """Test sorting a list with mixed-case strings."""
        input_data = ["banana", "Apple", "cherry"]
        expected = ["Apple", "banana", "cherry"]  # Case-sensitive sort
        self.assertEqual(sort_my_words(input_data), expected)

    def test_input_is_not_list(self):
        """Test that the function raises a TypeError if the input is not a list."""
        invalid_inputs = [None, 42, 3.14, True]
        for input_data in invalid_inputs:
            with self.assertRaises(TypeError):
                sort_my_words(input_data)

    def test_list_with_mixed_types(self):
        """Test handling a list with mixed types of elements (string and non-string)."""
        input_data = ["apple", "banana", None]
        with self.assertRaises(TypeError):
            sort_my_words(
                input_data
            )  # Should raise TypeError due to None being in the list

    def test_sorted_list_with_special_characters(self):
        """Test sorting a list that includes special characters."""
        input_data = ["banana", "apple", "#cherry", "@apple"]
        expected = [
            "#cherry",
            "@apple",
            "apple",
            "banana",
        ]  # Special characters come first
        self.assertEqual(sort_my_words(input_data), expected)


if __name__ == "__main__":
    unittest.main()
