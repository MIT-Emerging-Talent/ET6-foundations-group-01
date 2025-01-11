"""
A module for converting weights between kilograms and pounds.

This module provides two functions:
    - kilogram_to_pounds: Converts kilograms to pounds.
    - pounds_to_kilograms: Converts pounds to kilograms.

Module contents:
    - kilogram_to_pounds(kilograms: float) -> float: Converts kilograms to pounds.
    - pounds_to_kilograms(pounds: float) -> float: Converts pounds to kilograms.

Note:
The functions are mathematically valid for all numeric inputs,
including negative values. While negative weights may not be realistic in practice,
the module allows them for mathematical correctness.


Created on 2024-12-30
# My name may cause the linting error
Author: Olumide Kolawole
"""

# Conversion constants
KG_TO_LBS_CONVERSION_FACTOR = 2.20462
LBS_TO_KG_CONVERSION_FACTOR = 0.453592


def kilograms_to_pounds(kilograms: float) -> float:
    """
    Converts weight from kilograms to pounds using function name kilograms_to_pounds
    and also converts pounds to kilograms using function name pounds_to_kilograms.

    Parameters:
        kilograms (float): The weight in kilograms.
        The function works mathematically even if it's not realistic for
        real world weights

    Returns:
        kilogram_to_pounds(kilograms: float) -> float:
        The weight converted to pounds is,
        rounded to 3 decimal places for readability

     Raises:
        AssertionError: If the input is not a number (integer or float).

    Examples:
        >>> kilograms_to_pounds(0)
        0.0
        >>> kilograms_to_pounds(1)
        2.205
        >>> kilograms_to_pounds(-1)
        -2.205
        >>> kilograms_to_pounds(50)
        110.231
    """
    assert isinstance(
        kilograms, (int, float)
    ), "Input must be a number (integer or float)."
    pounds = kilograms * KG_TO_LBS_CONVERSION_FACTOR
    # Rounds to 3 decimal places
    return round(pounds, 3)


def pounds_to_kilograms(pounds: float) -> float:
    """
    Converts weight from pounds to kilograms.

    Parameters:
        pounds (float): The weight in pounds.

    Returns:
        pounds_to_kilograms(pounds: float) -> float:
        float: The weight converted to kilograms,
        rounded to 3 decimal places.

      Raises:
        AssertionError: If the input is not a number (integer or float).

    Examples:
        >>> pounds_to_kilograms(0)
        0.0
        >>> pounds_to_kilograms(2.205)
        1.0
        >>> pounds_to_kilograms(-2.205)
        -1.0
        >>> pounds_to_kilograms(110.231)
        50.0
    """
    assert isinstance(
        pounds, (int, float)
    ), "Input must be a number (integer or float)."
    kilograms = pounds * LBS_TO_KG_CONVERSION_FACTOR
    # Rounds to 3 decimal places
    return round(kilograms, 3)
