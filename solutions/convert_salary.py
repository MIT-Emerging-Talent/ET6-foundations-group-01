#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 2024-01-06

@author: Henry Ogoe
"""


def convert_salary(hourly: float, hours_per_week: float = 40) -> tuple:
    """
    Convert a hourly salary to monthly and yearly assuming full time (40 hours per week).

    Parameters:
        hourly (float): Hourly salary in dollars.
        hours_per_week: Amount of hours per week is set to 40. Added for flexibility.

    Returns:
        float: Monthly and yearly salary.

    Raises:
        AssertionError: If the input is not a float or salary is negative.

    >>> convert_salary(16.5)
    2857.8 34320.0

    >>> convert_salary(25)
    4333.0 51960.0

    >>> convert_salary(-40)
    Traceback (most recent call last):
    AssertionError: Salary cannot be negative.

    >>> convert_salary("7")
    Traceback (most recent call last):
    AssertionError: Inputs must be float.

    """

    assert isinstance(hourly, float), "Inputs must be float."
    assert hourly > 0, "Salary can not be negative."

    monthly_salary = hourly * hours_per_week * 4.33
    yearly_salary = hourly * hours_per_week * 52

    return (round(monthly_salary, 2), round(yearly_salary, 2))
