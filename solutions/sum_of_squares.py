#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Created 01-11-2025
@Author: Mithchell Cenatus

This module provides a function to calculate the sum of the squares of the numbers in a list.
"""

from typing import Union


def sum_of_square(numbers: list[Union[int, float]]) -> Union[int, float, None]:
    """
    Calculates the sum of the squares of the numbers in a list.

    Parameters:
        numbers (list[int | float]): The input list of numbers.

    Returns:
        int | float: The sum of the squares of the numbers in the provided list.
        None: If the input list is invalid.

    Raises:
        TypeError: If the input is not a list or contains invalid elements.

    Examples:
        >>> sum_of_square([1, 2, 3])
        14
        >>> sum_of_square([2.5, 1.1, 4])
        23.46
        >>> sum_of_square([-5.3, 9, -11, 2])
        23.09
        >>> sum_of_square([])
        0
    """
    if not isinstance(numbers, list):  # Ensure the input is a list
        raise TypeError("Input must be a list of integers and/or floats.")

    if not all(
        isinstance(num, (int, float)) for num in numbers
    ):  # Check if all elements are integers or floats
        raise TypeError("All elements in the list must be integers or floats.")

    if not numbers:  # Handle an empty list
        return 0

    # Calculate the sum of squares
    squares = (num**2 for num in numbers)  # Generator expression for efficiency
    total = sum(squares)  # Sum up all squared values
    return total
