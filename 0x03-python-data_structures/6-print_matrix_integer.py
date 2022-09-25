#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix == [[]]:
        print("{}".format("\n"))
    else:
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                print("{:d}".format(matrix[i][j]), end=" " if j <= 1 else "")
            print()
