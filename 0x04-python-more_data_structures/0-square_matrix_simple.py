#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    if matrix == [[]]:
        return [[]]
    r = []
    for i in range(len(matrix[0])):
        k = list(map(lambda x: x[i]*x[i], matrix))
        r.append(k)
    new = [[r[j][i] for j in range(len(r))] for i in range(len(r[0]))]
    return new
