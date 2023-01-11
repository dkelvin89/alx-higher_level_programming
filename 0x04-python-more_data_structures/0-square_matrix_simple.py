#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    result = []
    for i in matrix:
        square = list(map(lambda n: n * n, i))
        result.append(square)
    return (result)

"""
Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc.
"""