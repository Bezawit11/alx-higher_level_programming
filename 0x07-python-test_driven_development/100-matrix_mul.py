#!/usr/bin/python3
def matrix_mul(m_a, m_b):
    sum = 0
    lists = []
    ins = []
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not all(isinstance(a, list) for a in m_a):
        raise TypeError("m_a must be a list of lists") 
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(a, list) for a in m_b):
        raise TypeError("m_a must be a list of lists")
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    a = len(m_a[0])
    b = len(m_b[0])
    for i in range(len(m_a)):
        if len(m_a[i]) != a:
            raise TypeError("Each row of the matrix must have the same size")
    for i in range(len(m_b)):
        if len(m_b[i]) != b:
            raise TypeError("Each row of the matrix must have the same size")
    if len(m_a[len(m_a) - 1]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")
    for i in range(len(m_a)):
        for j in range(len(m_b[0])):
            for h in range(len(m_b)):
                if not isinstance(m_a[i][h], int) and not isinstance(m_a[i][h], float):
                    raise TypeError("m_a should contain only integers or floats")
                if not isinstance(m_b[i][h], int) and not isinstance(m_b[i][h], float):
                    raise TypeError("m_b should contain only integers or floats")
                sum = sum + (m_a[i][h] * m_b[h][j])
            ins.append(sum)
            sum = 0
        lists.append(ins)
        ins = []
    return lists
