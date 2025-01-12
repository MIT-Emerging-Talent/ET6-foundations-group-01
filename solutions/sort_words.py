#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created : 01-09-2025
@author : Mithchell Lawensky Cenatus

This function asks the user to provide a list of words
and returns the words sorted in alphabetical order, placing special characters before regular words.

"""


def sort_my_words(word_list):
    """
    Parameters:
        word_list (list): A list containing words as strings.

    Returns:
        list: A new list of words sorted in ascending order.

    Raises:
        TypeError: If the input is not a list of strings.

    Examples:
        >>> sort_my_words(["banana", "apple", "cherry"])
        ['apple', 'banana', 'cherry']

        >>> sort_my_words([])
        []

        >>> sort_my_words(["apple"])
        ['apple']

        >>> sort_my_words(["apple", 42])
        Traceback (most recent call last):
            ...
        TypeError: Invalid element 42 of type int. All elements must be strings.

        >>> sort_my_words("not a list")
        Traceback (most recent call last):
            ...
        TypeError: Input must be a list of strings.

        >>> sort_my_words(["banana", "apple", "#cherry", "@apple"])
        ['#cherry', '@apple', 'apple', 'banana']
    """
    # Ensure the input is a list of characters
    if not isinstance(word_list, list):
        raise TypeError("Input must be a list of strings.")

    # Ensure all elements are strings
    for word in word_list:
        if not isinstance(word, str):
            raise TypeError(
                f"Invalid element {word!r} of type {type(word).__name__}. All elements must be strings."
            )

    # Separate normal words and words with special characters
    regular_words = [word for word in word_list if word.isalpha()]
    special_words = [word for word in word_list if not word.isalpha()]

    # Sort each category separately
    sorted_regular_words = sorted(regular_words)
    sorted_special_words = sorted(special_words)

    # Combine results, special words come before normal words
    return sorted_special_words + sorted_regular_words
