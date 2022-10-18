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


matrix = [
        [1, 2, 3],
        [4, 5, 6,],
        [7, 8 , 9],
    ]
for i in range(3):
    for j in range(3):
        for z in range(3):
            for h in range(3):
                if z != i and h != j:
                    if checker(i , j , z, h, len(matrix)) == 1:
                        print(matrix[z][h], end="")
        print()            

