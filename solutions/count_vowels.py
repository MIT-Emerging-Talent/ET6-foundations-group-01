#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for counting vowels in a given string.

Module contents:
    - count_vowels: A function to count the number of vowels in a string (case-insensitive).

Created on 2024-12-27
Author: Yurii Spizhovyi
"""


def count_vowels(text: str) -> int:
    """
    Count_vowels function takes a string and count
    all upper and lower case vowels.

    Input: text[str]

    Return: num[int] the number of vowels in text

    >>> count_vowels("")
    0

    >>> count_vowels("0")
    0

    >>> count_vowels("what")
    1

    >>> count_vowels("Hello")
    2

    >>> count_vowels("Austria")
    4

    >>> count_vowels("Hello, World!")
    3
    """

    assert isinstance(text, str), "Input should be a string"

    list_vowels = ["a", "e", "i", "o", "u", "y"]
    count = sum(1 for char in text if char.lower() in list_vowels)
    return count
