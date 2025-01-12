#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module to divide two numbers and return the result.

Created 2025-01-04

@author: Henry Ogoe
"""


def divide_numbers(numerator: int, denominator: int) -> int:
    """Divides numerator by denominator and returns the quotient.

    Parameters:
    numerator(int): The first parameter
    denominator(int): The second parameter

    Returns:
    int: Result of division of numerator by denominator.

    Raises:
        TypeError: If the input contains non-integer elements.
        ValueError: If denominator is 0.

    Examples:
    >>> divide_numbers(4, 2)
    2
    >>> divide_numbers(64, 4)
    16

    >>> divide_numbers("4", 2)
    Traceback (most recent call last):
    TypeError: Inputs must be integers.

    >>> divide_numbers(8,0)
    Traceback (most recent call last):
    ValueError: Please dont divide by zero.
    """

    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Inputs must be integers.")
    if denominator == 0:
        raise ValueError("Please dont divide by zero.")
    return numerator // denominator
