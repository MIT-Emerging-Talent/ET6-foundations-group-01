#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for recursively calculating the sum of digits of an integer.

Module contents:
    - sum_of_digits: A recursive function to calculate the sum of digits.

Created on 2024-12-31
Author: Yurii Spizhovyi
"""


def sum_of_digits(number: int) -> int:
    """
    Recursively calculates the sum of digits of a given integer.

    Parameters:
        n (int): The positive integer to process. Assumes n >= 0.

    Returns:
        int: The sum of the digits in the given number.

    Raises:
        ValueError: If the input is negative.
        TypeError: If the input is not an integer.

    Examples:
        >>> sum_of_digits(1234)
        10
        >>> sum_of_digits(0)
        0
        >>> sum_of_digits(999)
        27
    """
    if not isinstance(number, int):
        raise TypeError("Input must be an integer.")
    if number < 0:
        raise ValueError("Input must be a non-negative integer.")

    # Base case: if the number is a single digit
    if number < 10:
        return number

    # Recursive case: add the last digit to the sum of remaining digits
    return (number % 10) + sum_of_digits(number // 10)
