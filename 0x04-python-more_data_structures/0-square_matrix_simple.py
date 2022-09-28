#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new = list(matrix)
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
           new[i][j] = matrix[i][j] * matrix[i][j]
    return new
