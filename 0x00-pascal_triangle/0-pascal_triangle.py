#!/usr/bin/python3
"""
A function that creates Pascal's Triangle.
"""


def pascal_triangle(n):
    """Creates A lit of Lists of Integers,
    that respresents Pascal's Triangle.
    """

    myTriangle = []
    if not isinstance(n, int) or n <= 0:
        return myTriangle

    for i in range(n):
        oneList = []
        for j in range(i + 1):
            if j == 0 or j == i:
                oneList.append(1)
            elif i > 0 and j > 0:
                oneList.append(myTriangle[i - 1][j - 1] + myTriangle[i - 1][j])
        myTriangle.append(oneList)
    return myTriangle
