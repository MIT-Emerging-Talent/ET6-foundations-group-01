#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
A module for converting binary strings to their decimal equivalents.

Module contents:
    - binary_to_decimal: Converts a binary string to its decimal representation.

Created on 2025-12-25
@author: Alemayehu_Desta
"""


def binary_to_decimal(binary_str: str) -> int:
    """
    Converts a binary string to its decimal equivalent.

    Parameters:
        binary_str (str): The binary string to convert. Must consist of '0' and '1' only.

    Returns:
        int: The decimal equivalent of the binary string.

    Raises:
        ValueError: If the input string is empty or contains characters other than '0' and '1'.

    Examples:
        >>> binary_to_decimal("101")
        5
        >>> binary_to_decimal("")
        Traceback (most recent call last):
        ValueError: Input must not be empty.
        >>> binary_to_decimal("102")
        Traceback (most recent call last):
        ValueError: Input must only contain '0' and '1'.
    """
    if not isinstance(binary_str, str):
        raise ValueError("Input must be a string.")
    if not binary_str:
        raise ValueError("Input must not be empty.")
    if not all(char in "01" for char in binary_str):
        raise ValueError("Input must only contain '0' and '1'.")

    return int(binary_str, 2)
