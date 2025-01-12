"""
Test for repeat_characters.py

Created 1/4/2025

Author: Dmytro Klymenko

"""

import unittest

from solutions.repeat_characters import repeat_characters


class TestRepeatedCharacters(unittest.TestCase):
    """This class deigned to test function repeat_characters.
    Function repeat all characters in word 2 times and return long word
    """

    def lower_case_char(self):
        """Test if will mulltiply lower characters"""
        self.assertEqual(repeat_characters("cash"), "ccaasshh")

    def test_multiple_char(self):
        """Test if will multipply same character twice"""
        self.assertEqual(repeat_characters("loop"), "lloooopp")

    def test_upper_case(self):
        """Test if will mulltiply upper characters"""
        self.assertEqual(repeat_characters("BOOM"), "BBOOOOMM")

    def test_upper_lower_case(self):
        """Test if will mulltiply upper and lower characters"""
        self.assertEqual(repeat_characters("MoThEr"), "MMooTThhEErr")

    def error_not_string(self):
        with self.assertRaises(AssertionError):
            repeat_characters(1)


if __name__ == "__main__":
    unittest.main()
