#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for multiplying two integers.

This module provides the multiply_two_numbers function, which multiplies
two integers and returns their product.

Module Contents:
    - multiply_two_numbers: A function to multiply two integers.

Created: 2025-01-04
Author: Manezhah Mohmand
"""


def multiply_two_numbers(num_one: int, num_two: int) -> int:
    """
    Multiplies two integers and returns the product.

    Parameters:
        num_one (int): The first integer.
        num_two (int): The second integer.

    Returns:
        int: The product of the two integers.

    Raises:
        TypeError: If either num_one or num_two is not an integer.

    Examples:
        >>> multiply_two_numbers(2, 3)
        6
        >>> multiply_two_numbers(-4, 5)
        -20
        >>> multiply_two_numbers(-2, -3)
        6
        >>> multiply_two_numbers(0, 10)
        0
    """
    # input validation for defensive test
    if not isinstance(num_one, int) or not isinstance(num_two, int):
        raise TypeError("Both arguments must be integers.")
    return num_one * num_two
