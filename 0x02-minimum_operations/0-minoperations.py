#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """method that calculates the fewest number of operations needed
    to result in exactly n H characters in a file"""
    if n < 2:
        return 0
    for i in range(2, n+1):
        if n % i == 0:
            return minOperations(int(n/i)) + i
