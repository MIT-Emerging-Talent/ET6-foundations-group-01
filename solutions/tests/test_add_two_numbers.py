"""Created 2025-01-03

@author: Yurii Spizhovyi

"""

import unittest
from solutions.add_two_numbers import add_numbers


class TestAddTwoNumbers(unittest.TestCase):
    """The test for testing add_numbers function."""

    def test_positive_numbers(self):
        """It should be positive numbers"""
        self.assertEqual(add_numbers(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
