def num_square(value):
    """
    Returns the square of a number.
    Args:
        value (int or float): The number to be squared.
    Returns:
        float: The square of the input number.
    Raises:
        AssertionError: If the input is not an int or float.
    Examples:
        >>> num_square(2)
        4.0
        >>> num_square(-3.5)
        12.25
    """
    # Ensure the input is valid
    assert isinstance(value, (int, float)), "Input must be an int or a float."
    # Calculate and return the square
    return float(value) ** 2
