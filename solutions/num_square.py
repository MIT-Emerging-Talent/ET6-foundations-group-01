"""
A module for calculating the square of a number.
Module contents:
    - num_square: A function to calculate the square of an integer or float.
Created 2025-01-04
@author: Manezhah Mohmand
"""


def num_square(value):
    """
    Returns the square of a number.
    Args:
        value (int or float): The number to be squared.
    Returns:
        float: The square of the input number.
    Raises:
        AssertionError: If the input is not an int or float.
    Examples:
        >>> num_square(2)
        4.0
        >>> num_square(-3.5)
        12.25
    """
    # Ensure the input is valid
    assert isinstance(value, (int, float)), "Input must be an int or a float."
    # Calculate and return the square
    return float(value) ** 2
