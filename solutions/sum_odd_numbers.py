#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting the sum of only odd numbers in a provided list.

Module contents:
    - sum_odd_numbers: A function to calculate the sum of odd numbers in a provided list.

Created on 2025-01-02
@author: Sukhrob Muborakshoev
"""


def sum_odd_numbers(numbers: list[int]) -> int | None:
    """
    Calculate the sum of only odd numbers in a given list.

    Parameters:
    numbers (list[int]): The input list of integers.

    Returns:
    int: The sum of all odd numbers in the provided list.
    None: If the list is invalid.

    Raises:
    TypeError: If the input is not a list.

    Examples:
    >>> sum_odd_numbers([1, 2, 3, 4, 5])
    9
    >>> sum_odd_numbers([2, 4, 6, 8])
    0
    >>> sum_odd_numbers([1, -3, 5, -7])
    -4
    >>> sum_odd_numbers([])
    0
    """
    if numbers is None:
        raise TypeError("The function requires a list of integers as an argument.")

    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    if not all(isinstance(num, int) for num in numbers):
        return None

    total = 0
    for num in numbers:
        if num % 2 != 0:
            total += num
    return total
