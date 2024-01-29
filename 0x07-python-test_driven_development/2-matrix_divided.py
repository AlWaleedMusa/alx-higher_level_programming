#!/usr/bin/python3

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a given number.

    Args:
        matrix (list of lists): Matrix of integers or floats.
        div (int or float): Number to divide each element of the matrix by.

    Returns:
        list of lists: New matrix with elements rounded to 2 decimal places.

    Raises:
        TypeError: If the matrix is not a list of lists of integers or floats.
        TypeError: If each row of the matrix does not have the same size.
        TypeError: If div is not a number (integer or float).
        ZeroDivisionError: If div is equal to 0.
    """
    # Check if arguments are percent
    if matrix == None or div == None:
        raise TypeError("Argument missing")
    # Check if matrix is a list of lists
    if not all(isinstance(row, list) for row in matrix) or not all(isinstance(element, (int, float)) for row in matrix for element in row):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    
    # Check if each row of the matrix has the same size
    if len(set(len(row) for row in matrix)) > 1:
        raise TypeError("Each row of the matrix must have the same size")
    
    # Check if div is a number (integer or float)
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    
    # Check if div is not equal to 0
    if div == 0:
        raise ZeroDivisionError("division by zero")
    
    
    # Divide each element of the matrix by div, rounded to 2 decimal places
    result_matrix = [[round(element / div, 2) for element in row] for row in matrix]
    
    return result_matrix
