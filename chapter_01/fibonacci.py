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


# Using iteration and tuple unpacking
def  fib5(n:int) -> int:
    if n ==0 :
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next


# Using a Generator
from typing import Generator

def fib6(n: int) -> Generator[int, None, None]:
    yield 0 # special case
    if n > 0: yield 1
    last: int = 0  # initally set to fib(0)
    next: int = 1  # initially set to fib(1)
    for _ in range(1, n):
        last, next = next, last + next
        yield next # main generation step 

if __name__ == "__main__":
    # print(fib_recursive(7))
    print(fib3(50))

    print(fib4(50))

    print(fib5(50))

    for i in fib6(50):
        print(i)
