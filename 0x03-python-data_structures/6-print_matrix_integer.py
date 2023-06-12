#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        i_end = ""
        for j in range(len(i)):
            i_end += "{:d}".format(i[j])
            if j != len(i) - 1:
                i_end += " "
        print(i_end)
