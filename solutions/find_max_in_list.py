#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for finding the maximum value in a list of integers.

Module contents:
    - find_max_in_list: A function to find the maximum number in a list.

Created 2024-12-27

@author: Yurii Spizhovyi
"""


def find_max_in_list(numbers: list[int]) -> int | None:
    """
    Find and return the maximum number in a given list.

    Args:
        numbers (list[int]): A list of integers.

    Returns:
        int: The maximum number in the list.
        None: If the list is empty.

    Raises:
        TypeError: If the input is not a list or if the list contains non-integer elements.

    Tests:

    >>> print(find_max_in_list([]))
    None

    >>> print(find_max_in_list([0, 0]))
    0

    >>> print(find_max_in_list([1, 2, 3]))
    3

    >>> find_max_in_list("not a list")
    Traceback (most recent call last):
    TypeError: Input must be a list of integers

    >>> find_max_in_list([1, "2", 3])
    Traceback (most recent call last):
    TypeError: All elements in the list must be integers
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers")
    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers")
    if not numbers:  # Handle empty list explicitly
        return None
    return max(numbers)
