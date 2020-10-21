from functools import lru_cache
import math

__all__ = ['my_sum', 'factorial']


def my_sum(iterable):
    """Sum implemetnation."""
    tot = 0
    for i in iterable:
        tot += i
    return tot


@lru_cache(maxsize=None)  # Note: -> @cache in python >= 3.9
def factorial(n):
    """Factorial function implementation."""
    return n * factorial(n-1) if n else 1


def sin(x):
    """Sine function implementation."""
    sum = 0
    for a in range(100):
        sum += (math.pow(-1, a))/(factorial(2*a+1))*(math.pow(x, 2*a+1))
    return sum
