#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Unit tests for the binary_to_decimal module."""

import unittest

from solutions.binary_to_decimal import binary_to_decimal


class TestBinaryToDecimal(unittest.TestCase):
    """Tests for the binary_to_decimal function."""

    def test_valid_binary(self):
        """Test conversion of valid binary strings."""
        self.assertEqual(binary_to_decimal("101"), 5)

    def test_zero_binary(self):
        """Test conversion of the binary string '0'."""
        self.assertEqual(binary_to_decimal("0"), 0)

    def test_all_ones_binary(self):
        """Test conversion of a binary string with all ones."""
        self.assertEqual(binary_to_decimal("1111"), 15)

    def test_invalid_binary_non_binary_characters(self):
        """Test with invalid binary strings containing non-binary characters."""
        with self.assertRaises(ValueError):
            binary_to_decimal("102")

    def test_invalid_binary_empty_string(self):
        """Test with an empty binary string."""
        with self.assertRaises(ValueError):
            binary_to_decimal("")

    def test_invalid_binary_non_string_input(self):
        """Test with non-string input."""
        with self.assertRaises(ValueError):
            binary_to_decimal(101)


if __name__ == "__main__":
    unittest.main()
