#!/usr/bin/python3
"""Find the Minumum Operations"""


def minOperations(n):
    """
    @n: number of characters
    Return: the number of minimum operations
    """
    curr = 1
    count = 0
    clipboard = 0

    while curr < n:
        rest = n - curr

        if rest % curr == 0:
            clipboard = curr
            curr += clipboard
            count += 2
        else:
            curr += clipboard
            count += 1
    return count
