#!/usr/bin/python3
"""Rotate A 2D Matrix"""


def rotate_2d_matrix(matrix: list):
    """returns A rotated 2D Matrix"""
    n = len(matrix)
    for i in range(n // 2):
        for j in range(i, n - i - 1):
            tmp = matrix[i][j]
            matrix[i][j] = matrix[n - j - 1][i]
            matrix[n - j - 1][i] = matrix[n - i - 1][n - j - 1]
            matrix[n - i - 1][n - j - 1] = matrix[j][n - i - 1]
            matrix[j][n - i - 1] = tmp
