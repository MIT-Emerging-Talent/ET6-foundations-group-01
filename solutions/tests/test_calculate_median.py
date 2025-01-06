"""
Unit Test for Calculate Median Function
This file tests the `calculate_median` function, ensuring it behaves
as expected with various valid and invalid inputs.
Created on 01/03/2025
Author: Khadija Al Ramlawi
"""

import unittest
from solutions.calculate_median import calculate_median


class TestCalculateMedian(unittest.TestCase):
    """
    Test cases to validate the functionality of the calculate_median function.
    """

    def test_odd_length_list(self):
        # Test case for an odd-length list.
        self.assertEqual(calculate_median([1, 3, 2]), 2.0)

    def test_even_length_list(self):
        # Test case for an even-length list.
        self.assertEqual(calculate_median([4, 1, 7, 8]), 5.5)

    def test_single_element(self):
        # Test case for a single-element list.
        self.assertEqual(calculate_median([5]), 5.0)

    def test_empty_list(self):
        # Test case for an empty list.
        with self.assertRaises(AssertionError):
            calculate_median([])

    def test_non_numeric_elements(self):
        # Test case for a list with non-numeric elements.
        with self.assertRaises(AssertionError):
            calculate_median([1, "a", 3])

    def test_non_list_input(self):
        # Test case for a non-list input.
        with self.assertRaises(AssertionError):
            calculate_median("not a list")

    def test_sorted_input(self):
        # Test case for an already sorted list.
        self.assertEqual(calculate_median([1, 2, 3, 4]), 2.5)

    def test_unsorted_input(self):
        # Test case for an unsorted list.
        self.assertEqual(calculate_median([4, 1, 3, 2]), 2.5)


if __name__ == "__main__":
    unittest.main()
