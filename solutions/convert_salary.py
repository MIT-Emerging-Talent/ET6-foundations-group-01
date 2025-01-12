#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module for converting an hourly wage to its equivalent monthly and yearly salaries.

Module contents:
    - convert_salary: A function to convert an hourly wage and
calculates the monthly and yearly salaries.

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
        tuple: Monthly and yearly salary rounded to 2 decimals.

    Raises:
        AssertionError: If the input is not a float or salary is negative.

    >>> convert_salary(16.5)
    (2857.8, 34320.0)

    >>> convert_salary(25)
    (4330.0, 52000)

    >>> convert_salary(1000000)
    (173200000.0, 2080000000)

    >>> convert_salary(0.1)
    (17.32, 208.0)

    >>> convert_salary(16.5, 100)
    (7144.5, 85800.0)

    >>> convert_salary(-8)
    Traceback (most recent call last):
    AssertionError: Salary can not be negative.

    >>> convert_salary("7")
    Traceback (most recent call last):
    AssertionError: Inputs must be float.

    """

    assert isinstance(hourly, (float, int)), "Inputs must be float."
    assert hourly > 0, "Salary can not be negative."

    monthly_salary = hourly * hours_per_week * 4.33
    # 4.33 is approximate number of weeks in month
    yearly_salary = hourly * hours_per_week * 52
    # We have 52 weeks in a year

    return (round(monthly_salary, 2), round(yearly_salary, 2))
