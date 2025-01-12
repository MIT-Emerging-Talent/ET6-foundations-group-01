#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-28

@author: Mykyta Kondratiev
"""


def even_numbers(numbers: list) -> bool:
    """
    All_even function checks if all numbers in a list are even.

    Input: numbers[list]

    Return: result[bool] True if all numbers are even, False otherwise

    >>> even_numbers([])
    True

    >>> even_numbers([2, 4, 6])
    True

    >>> even_numbers([2, 3, 6])
    False

    >>> even_numbers([0, -2, 8])
    True

    >>> even_numbers([1])
    False
    """
    # Assertions for input validation
    assert numbers is not None, "Input cannot be None"
    assert isinstance(numbers, list), "Input should be a list"
    assert all(isinstance(num, int) for num in numbers), (
        "All elements in the list must be integers"
    )

    # Check if all elements are even
    return all(num % 2 == 0 for num in numbers)
