#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created 01-05-2025
@author: Mithchell Cenatus

This function calculates the average of a list of integers.
"""

from typing import (
    Union,
)  # For type annotations compatible with older versions of Python


def calculate_average(numbers: list[int]) -> Union[float, None]:
    """
    Calculates the average of a list of integers.

    Parameters:
        numbers (list[int]): The input list of integers.

    Returns:
        float: The average of all numbers in the provided list.
        None: If the list is empty or contains invalid elements.

    Raises:
        TypeError: If the input is not a list or contains non-integer elements.

    Examples:
    >>> calculate_average([1, 2, 3, 4, 5, 6])
    3.5
    >>> calculate_average([2, 4, 6])
    4.0
    >>> calculate_average([1, 3, 5, 7, 9])
    5.0
    """
    if not isinstance(numbers, list):
        raise TypeError("Input must be a list of integers.")

    if not all(isinstance(num, int) for num in numbers):
        raise TypeError("All elements in the list must be integers.")
    if not numbers:
        return None

    # Calculate and return the average
    return sum(numbers) / len(numbers)
