#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
This module contains a function that implements the FizzBuzz game logic.

Created on 2025-05-01
@author: Alemayehu Desta
"""

from typing import List


def fizzbuzz(n: int) -> List[str]:
    """
    Generates a list of strings representing the FizzBuzz sequence from 1 to n.

    Parameters:
        n (int): The upper limit of the FizzBuzz sequence. Must be a positive integer.

    Returns:
        List[str]: A list of strings where:
                - Multiples of 3 are replaced by "Fizz".
                - Multiples of 5 are replaced by "Buzz".
                - Multiples of both 3 and 5 are replaced by "FizzBuzz".
                - Other numbers are converted to their string representation.

    Raises:
        ValueError: If `n` is not a positive integer.

    Examples:
        >>> fizzbuzz(5)
        ['1', '2', 'Fizz', '4', 'Buzz']

        >>> fizzbuzz(15)
        ['1', '2', 'Fizz', '4', 'Buzz', 'Fizz', '7', '8', 'Fizz', 'Buzz', '11', 'Fizz', '13', '14', 'FizzBuzz']

        >>> fizzbuzz(0)
        Traceback (most recent call last):
        ...
        ValueError: n must be a positive integer.
    """
    if not isinstance(n, int):
        raise ValueError("n must be an integer.")
    if n <= 0:
        raise ValueError("n must be a positive integer.")

    result = []
    for i in range(1, n + 1):
        if i % 3 == 0 and i % 5 == 0:
            result.append("FizzBuzz")
        elif i % 3 == 0:
            result.append("Fizz")
        elif i % 5 == 0:
            result.append("Buzz")
        else:
            result.append(str(i))
    return result
