#!/usr/bin/python3
"""consider it as useful documentation please"""


def makeChange(coins, total):
    """consider it as a useful documentation idk"""
    if total <= 0:
        return 0

    chk, mvoes = 0, 0
    coins.sort(reverse=True)

    for coin in coins:
        while chk < total:
            chk += coin
            mvoes += 1

        if chk == total:
            return mvoes

        chk -= coin
        mvoes -= 1

    return -1
