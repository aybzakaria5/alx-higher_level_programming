#!/usr/bin/python3
""" a function that divides all the elements of a matrix
"""


def matrix_divided(matrix, div):
    """divides all elemnets of a mtarix

    Args:
        matrix ([int/float]): a list of lists
        div ([int/float]): a number to divide

    Returns:
        a matrix after dividing elemnts
    """

    div_matrix = [[]]
    if not all(
        isinstance(matrix, list) and
        all(isinstance(elem, (int, float)) for elem in row)
        for row in matrix
    ):
        raise TypeError("matrix must be a matrix\
            (list of lists) of integers/floats")

    for row in matrix:
        if len(row) != len(matrix[0]):
            raise TypeError("Each row of the matrix must have the same size")
    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    elif div == 0:
        raise ZeroDivisionError("division by zero")
    else:
        div_matrix = [[round(elem / div, 2) for elem in row] for row in matrix]

    return div_matrix
