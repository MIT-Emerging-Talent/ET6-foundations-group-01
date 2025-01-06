"""
Calculates the Median of a List of Numbers
This file contains a function to calculate the median of a list of numbers.
Created on 01/03/2025
Author: Khadija Al Ramlawi
"""


def calculate_median(numbers: list) -> float:
    """
    Calculates the median of a list of numbers.
    Parameters:
        numbers (list): A list of numeric values.
    Returns:
        float: The median value of the list.
    Raises:
        AssertionError: If the input is not a list.
        AssertionError: If the input contains non-numeric values.
        AssertionError: If the input list is empty.
    Examples:
        >>> calculate_median([1, 3, 2])
        2.0
        >>> calculate_median([4, 1, 7, 8])
        5.5
        >>> calculate_median([5])
        5.0
    """
    assert isinstance(numbers, list), "Input must be a list."
    assert all(
        isinstance(num, (int, float)) for num in numbers
    ), "All elements in the list must be numeric."
    assert len(numbers) > 0, "Input list cannot be empty."

    sorted_numbers = sorted(numbers)
    n = len(sorted_numbers)

    if n % 2 == 1:
        return sorted_numbers[n // 2]
    else:
        mid1 = sorted_numbers[n // 2 - 1]
        mid2 = sorted_numbers[n // 2]
        return (mid1 + mid2) / 2
