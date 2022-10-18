#!/usr/bin/python3
def matrix_divided(matrix, div):
    mylist = []
    ins = []
    if not isinstance(div, int) and not isinstance(div, float):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    if not isinstance(matrix, list) or not all(isinstance(a, list) for a in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for i in range(len(matrix)):
        if i != 0 and len(matrix[i]) != len(matrix[i - 1]):
            raise TypeError("Each row of the matrix must have the same size")
        for j in range(len(matrix[i])):
            if not isinstance(matrix[i][j], int) and not isinstance(matrix[i][j], float):
                raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
            ins.append(round(matrix[i][j] / div, 2))
        mylist.append(ins)
        ins = []
    return mylist
