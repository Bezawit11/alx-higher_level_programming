#!/usr/bin/python3
def search_replace(my_list, search, replace):
    mat = my_list.copy()
    for i in range(len(mat)):
        if mat[i] == search:
            mat[i] = replace
    return mat
