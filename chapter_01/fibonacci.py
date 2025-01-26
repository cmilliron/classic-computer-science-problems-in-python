"""
The Fibonacci sequence is a sequence of numbers such that any number, except for the first and second, is the sum of the previous two:

0, 1, 1, 2, 3, 5, 8, 13, 21...
"""

# Recursive attempt

def fib_recursive(n:int) -> int:
    if n < 2: #Base case
        return n
    return fib_recursive(n-1) + fib_recursive(n-2)

from typing import Dict
memo: Dict[int, int] = {0: 0, 1: 1}

def fib3(n:int) -> int:
    if n not in memo:
        memo[n] = fib3(n-1) + fib3(n-2)
    return memo[n]


from functools import lru_cache

@lru_cache #Will cache and return the cached value
def fib4(n:int) -> int:
    if n < 2: #Base case
        return n
    return fib4(n-1) + fib4(n-2)


if __name__ == "__main__":
    # print(fib_recursive(7))
    print(fib3(50))

    print(fib4(50))
