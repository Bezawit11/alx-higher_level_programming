#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == None:
        print()
        return
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            print("{}".format(matrix[i][j]), end=" ")
        print()
