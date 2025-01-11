#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-29

@author: Yuri Spizhovyi
"""


def convert_fahrenheit_to_celsius(fahrenheit: float) -> float:
    """
    Convert a temperature from Fahrenheit to Celsius.

    Parameters:
        fahrenheit (float): The temperature in Fahrenheit.

    Returns:
        float: The temperature in Celsius.

    Raises:
        AssertionError: If the input is not a float or an int.

    >>> convert_fahrenheit_to_celsius(32)
    0.0

    >>> convert_fahrenheit_to_celsius(212)
    100.0

    >>> convert_fahrenheit_to_celsius(-40)
    -40.0

    >>> convert_fahrenheit_to_celsius(98.6)
    37.0
    """
    assert isinstance(fahrenheit, (int, float)), (
        "Input must be a number (int or float)."
    )
    return round((fahrenheit - 32) * 5.0 / 9.0, 1)
