#!/usr/bin/python3
l = []
ins = []
for i in range(3):
    for j in range(3):
        for z in range(3):
            for h in range(3):
                if z != i and h != j:  #can't be the same r & c
                    if z != i + a or h != j + a or z != i - a or h != j - a or z != i - a or h != j + a or z != i + a or h != j - a:
                        print(m[z][h], end="")
                        a += 1
        print()
