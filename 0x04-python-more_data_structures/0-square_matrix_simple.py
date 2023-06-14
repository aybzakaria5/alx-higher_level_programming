#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    sq_matrix = list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
    return sq_matrix
