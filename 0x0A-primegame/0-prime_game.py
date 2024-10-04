#!/usr/bin/python3
"""
prime time task
"""


def isWinner(x, nums):
    """
    main function for prime game module
    """
    maria = 0
    ben = 0

    def SieveOfEratosthenes(n):
        """Sieve of Eratosthenes Function"""

        prime = [True for i in range(n + 1)]
        pointer = 2
        while pointer * pointer <= n:
            if prime[pointer] is True:
                for i in range(pointer * pointer, n + 1, pointer):
                    prime[i] = False
            pointer += 1
        prime[0] = False
        prime[1] = False
        return prime

    max_n = max(nums)
    primes = SieveOfEratosthenes(max_n)

    for round in nums:
        round_primes = [i for i in range(round + 1) if primes[i]]
        if len(round_primes) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if maria > ben:
        return "Maria"
    elif ben > maria:
        return "Ben"

    return None