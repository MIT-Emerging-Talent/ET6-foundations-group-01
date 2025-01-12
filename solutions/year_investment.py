"""
Year Investment

1/8/2025

created by Dmytro Klymenko

"""


def year_investment(number, percentage: int) -> float:
    """
    Function is designed to calculate yearly income with desired
    amount and percentage

    Args:
        number (int): Amount of money to be invested
        percentage (int): Year percantage

    Returns:
      int - Final amount of money after year investment

    Raises:
      AssertionError: if the number or percentage is not a
      float or an int.

    Examples:

    >>> year_investment(10000, 5)
    10500.0
    >>> year_investment(100, 2)
    102.0
    >>> year_investment(278, 3)
    286.34
    """
    assert isinstance(number, (int, float))
    assert isinstance(percentage, (int, float))
    assert number >= 0
    assert percentage >= 0

    return number * (percentage / 100) + number
