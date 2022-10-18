#!/usr/bin/python3
def checker(i , j , z, h, l):
    for k in range(1, l):
        if z != i + k or h != j + k:
            continue
        else:
            return 0
    for k in range(1, l):
        if z != i - k or h != j + k:
            continue
        else:
            return 0;
            
    for k in range(1, l):
        if z != i - k or h != j - k:
            continue
        else:
            return 0
            
    for k in range(1, l):
        if z != i + k or h != j - k:
            continue
        else:
            return 0
    return 1

def queen(matrix):
    l = []
    ins = []
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            for z in range(len(matrix)):
                for h in range(len(matrix)):
                    if z != i and h != j:
                        if checker(i , j , z, h, len(matrix)) == 1:
                            print(matrix[z][h], end=",") 
            print(" for " + str(i) + " and " + str(j)) 

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

queen(matrix)
