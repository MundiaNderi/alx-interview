#!/usr/bin/python3
"""
Rotates an n by n 2D matrix 90 degrees
clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Don't return anything.
    Matrix must be edited in place.
    Assume matrix will have 2 dimensions and will
    not be empty
    """

    # First Transpose the matrix
    for i in range(len(matrix)):
        for j in range(i, len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Then reverse the matrix(row elements)
    N = len(matrix)
    for i in range(N // 2):
        for j in range(N):
            matrix[j][i], matrix[j][N-1-i] = matrix[j][N-1-i], matrix[j][i]
