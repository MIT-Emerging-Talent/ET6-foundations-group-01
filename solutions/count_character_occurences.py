#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-12-29

@author: Sukhrob Muborakshoev
"""


def count_character_occurrences(text: str, char: str | None) -> int | str:
    """
    Count the occurrences of a specific character in a string.

    Parameters:
    text (str): The input string.
    char (str): The character to count (must be a single character).

    Returns:
    int: The number of times the specified character appears in the string.
    str: The string itself if second parameter is None

    Raises:
    ValueError: If the char parameter is not a single character.

    Examples:
    >>> count_character_occurrences("hello world", "l")
    3
    >>> count_character_occurrences("python programming", "p")
    2
    >>> count_character_occurrences("", "a")
    0
    >>> count_character_occurrences("mit")
    mit
    """
    if char is None:
        return text

    if len(char) != 1:
        raise ValueError("The char parameter must be a single character.")

    count = 0
    for current_char in text:
        if current_char == char:
            count += 1

    return count