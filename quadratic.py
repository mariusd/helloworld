"""Module contains a function that solves quadratic equation."""

import math

def solve_quadratic(a, b, c):
    """Find real or complex roots of equation ax**2 + bx + c = 0.

    >>> solve_quadratic(0, 2, 1)
    Traceback (most recent call last):
    ...
    ValueError: equation is not quadratic

    >>> solve_quadratic(1, -4, 4)
    (2.0,)

    >>> solve_quadratic(1, -5, 6)
    (2.0, 3.0)

    >>> [solve_quadratic(1, 0, k**2) for k in range(1, 5)]
    [(-1j, 1j), (-2j, 2j), (3j, -3j), (4j, -4j)]
    """
    if a == 0:
        raise ValueError("equation is not quadratic")
    discriminant = b**2 - 4 * a * c
    sqrt = lambda x : math.sqrt(x) if x >= 0 else complex(0, math.sqrt(-x))
    roots = ((-b + k * sqrt(discriminant)) / (2.0 * a) for k in (-1, 1))
    return tuple(set(roots))

if __name__ == "__main__":
    import doctest
    doctest.testmod()
