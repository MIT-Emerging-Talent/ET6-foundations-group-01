"""
A  module for multiplying two integers.

Module contents:
     - multiply_two_numbers: A function to multiply two integers.
created  2025-01-04
@author: Manezhah Mohmand
"""


def multiply_two_numbers(a: int, b: int) -> int:
    """Multiplies two integers and returns the product.
g
    parameters:
     a (int): The  first integer
     b (int):The second  integer

     Returns:
     int: The product of the two integers

     Raises:
         TypeError:If the input contains non-integer elements.
    Examples:
    >>> multiply_two_numbers(2, 3)
    6
    """
    
    #Raise an error if a and b are not integers
    if not isinstance(a, int) or not isinstance(b, int):
        raise TypeError("Both arguments must be integers.")
    return a * b
