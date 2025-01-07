#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A module for calculating Body Mass Index (BMI).

This module provides a function to calculate BMI based on a person's weight
and height and classify the result into categories:
    - Underweight
    - Normal
    - Overweight
    - Obese

Module contents:
    - calculate_and_classify_bmi(weight_kg: float, height_m: float) ->tuple[str, float]:
        Calculates BMI based on weight (in kg) and height (in meters)
        and classifies it.

Raises:
    - AssertionError: If inputs are not numbers (int or float).
    - ValueError: If weight or height is non-positive.

Note:
    - Inputs must be positive numbers. If the inputs are invalid,
      the function will return None with an appropriate message.
    - The BMI calculation is mathematically valid for all positive inputs.
    - Extremely large or small inputs may produce unrealistic results.
    - BMI calculation is rounding to one due to general convention

Created on 2025-1-4
Author: Olumide Kolawole
"""


def calculate_and_classify_bmi(weight_kg: float, height_m: float) -> tuple[str, float]:
    """
    Calculates the Body Mass Index (BMI) and classifies it.

    Parameters:
        weight_kg (float): Weight in kilograms.
        height_m (float): Height in meters.

    Returns:
        tuple (str, float)
        tuple containing the BMI category
        and the calculated BMI rounded to one decimal place
    Raises:
        - AssertionError: If inputs are not numbers (int or float).
        - ValueError: If weight or height is non-positive.

    Categories:
        - BMI < 18.5: Underweight
        - 18.5 <= BMI < 25: Normal
        - 25 <= BMI < 30: Overweight
        - BMI >= 30: Obese

    Examples:
        >>> calculate_and_classify_bmi(70, 1.75)
        ('Normal', 22.9)
        >>> calculate_and_classify_bmi(50, 1.8)
        ('Underweight', 15.4)
        >>> calculate_and_classify_bmi(95, 1.6)
        ('Obese', 37.1)
        >>> calculate_and_classify_bmi(-70, 1.75)
        Traceback (most recent call last):
            ...
        ValueError: Weight and height must be positive numbers.
    """

    # Validate inputs
    assert isinstance(weight_kg, (int, float))
    assert isinstance(height_m, (int, float))

    if weight_kg <= 0 or height_m <= 0:
        raise ValueError("Weight and height must be positive numbers.")

    # Calculate BMI
    bmi = weight_kg / (height_m**2)

    # Classify BMI
    if bmi < 18.5:
        bmi_category = "Underweight"
    elif bmi < 25:
        bmi_category = "Normal"
    elif bmi < 30:
        bmi_category = "Overweight"
    else:
        bmi_category = "Obese"

    # Return BMI category and rounded BMI value
    return bmi_category, round(bmi, 1)
