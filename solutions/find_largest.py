"""
Finds the Largest Number in a List
This file contains a function to find the largest number in a given list of numbers.
Created on 01/10/2025
Author: Khadija Ramlawi
"""


def find_largest(numbers: list) -> int:
    """
    Finds the largest number in the given list.
    Parameters:
        numbers (list): A list of numeric values.
    Returns:
        int: The largest number in the list.
    Raises:
        AssertionError: If the input is not a list.
        AssertionError: If the input list is empty.
        AssertionError: If the input contains non-numeric values.
    Examples:
        >>> find_largest([1, 2, 3])
        3
        >>> find_largest([10, 20, 30, 40])
        40
        >>> find_largest([-5, -1, -10])
        -1
    """
    assert isinstance(numbers, list), "Input must be a list."
    assert len(numbers) > 0, "List cannot be empty."
    assert all(
        isinstance(num, (int, float)) for num in numbers
    ), "All elements must be numeric."

    return max(numbers)
