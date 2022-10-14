#!/usr/bin/python3
def matrix_divided(matrix, div):
    list = []
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                list.append(matrix[i][j] / div)
    return list
