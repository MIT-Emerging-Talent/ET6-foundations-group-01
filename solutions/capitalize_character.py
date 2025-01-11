"""
Capitalize character Function

Created on 12/28/2024

Author : Khadija Ramlawi
"""


def capitalize_character(text: str, char_to_capitalize: str) -> str:
    """
    Capitalizes a specified character in a given string

    Parameters:
        text (str): The string in which the character will be capitalized.
        char_to_capitalize (str): The character to capitalize. Must be a single character.

    Returns:
        str: The string with the specified character capitalized.

    Raises:
        AssertionError: If the first argument is not a string.
        AssertionError: If the second argument is not a string.
        AssertionError: If the second argument is not a single character.

    Examples:
        >>> capitalize_character('cat', 'a')
        'cAt'

        >>> capitalize_character('hello', 'l')
        'heLLo'

        >>> capitalize_character('rose', 'a')
        'rose'
    """
    assert isinstance(text, str), "Input should be a string."
    assert isinstance(char_to_capitalize, str), "Input should be a string."
    assert len(char_to_capitalize) == 1, (
        "Character to capitalize must be a single character."
    )

    capitalized_text = ""

    for char in text:
        if char.lower() == char_to_capitalize.lower():
            capitalized_text += char.upper()
        else:
            capitalized_text += char

    return capitalized_text
