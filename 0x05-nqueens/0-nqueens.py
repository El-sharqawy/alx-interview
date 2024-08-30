#!/usr/bin/python3
"""
N-Queens Chess Answer Script.
"""

import sys


def nqueens_helper(num, y, board):
    """
    backtracking function.
    """
    for i in range(num):
        breakPoint = 0
        for j in board:
            if i == j[1] or abs(i - j[1]) == abs(y - j[0]):
                breakPoint = 1
                break
        if breakPoint == 0:
            board.append([y, i])
            if y == num - 1:
                print(board)
            else:
                nqueens_helper(num, y + 1, board)
            board.pop()


def nqueens(num):
    """
    Solve the N-Queens n x n Chess.
    """
    board = []
    nqueens_helper(num, 0, board)


def main():
    """
    Main, Entry Point
    """
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        num = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        exit(1)
    if num < 4:
        print("N must be at least 4")
        exit(1)
    nqueens(num)


if __name__ == "__main__":
    main()
