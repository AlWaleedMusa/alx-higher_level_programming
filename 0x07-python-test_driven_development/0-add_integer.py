#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Defaults to 98.

    Returns:
        int: The addition of a and b.
        
    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if a is None:
        raise TypeError("missing 1 required positional argument 'a'")

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)