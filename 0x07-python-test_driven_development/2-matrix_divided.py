#!/usr/bin/python3
def matrix_divided(matrix, div):
    list = []
    ins = []
    for i in range(len(matrix)):
        if i != 0 and len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            else:
                ins.append(matrix[i][j] / div)
        list.append(ins)
        ins = []
    return list
