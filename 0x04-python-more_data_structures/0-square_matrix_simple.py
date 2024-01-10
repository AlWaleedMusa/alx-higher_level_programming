#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_list = []
    for i in range(len(matrix)):
        li = [num * num for num in matrix[i]]
        new_list.append(li)
    return (new_list)
