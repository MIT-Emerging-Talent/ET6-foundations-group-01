"""
A module for calculating the sum of integer.

Module contents:
    - sum_of_digits: A function to calculate the sum of 2 digits.

Created 2024-01-03

@author: Yurii Spizhovyi
"""


def add_numbers(a: int, b: int) -> int:
    """Adds two numbers and returns their sum.

    Parameters:
    a(int): The first integer
    b(int): The second integer

    Returns:
    int: The sum of the two integers

    Raises:
        TypeError: If the input contains non-integer elements.

    Examples:
    >>> add_numbers(1, 2)
    3
    >>> add_numbers(-1, 2)
    1

    >>> add_numbers("1", 2)
    Traceback (most recent call last):
    TypeError: Inputs must be integers.
    """

    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Inputs must be integers.")
    return a + b
