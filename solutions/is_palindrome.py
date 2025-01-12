#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2025-01-03
@author: Mykyta Kondratiev
"""


def is_palindrome(s: str = "") -> bool:
    """
    Function to check if a string is a palindrome.
    Input: s[str] (optional, default empty string)
    Return: result[bool] True if the string is a palindrome, False otherwise

    >>> is_palindrome('racecar')
    True
    >>> is_palindrome('hello')
    False
    >>> is_palindrome('')
    True
    >>> is_palindrome('A man a plan a canal Panama')
    True
    >>> is_palindrome('Was it a car or a cat I saw?')
    True
    >>> is_palindrome()
    True  # when no argument is passed, assumes empty string
    """
    # Assertions for input validation
    assert s is not None, "Input cannot be None"
    assert isinstance(s, str), "Input should be a string"

    # Normalize the string: remove non-alphanumeric characters and convert to lowercase
    cleaned = "".join(char.lower() for char in s if char.isalnum())

    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]
