#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    new_m = []
    for i in matrix:
        new_r = list(map(lambda x: x ** 2, i))
        new_m.append(new_r)
    return new_m
