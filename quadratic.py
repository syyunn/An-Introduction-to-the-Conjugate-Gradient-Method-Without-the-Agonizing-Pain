"""
Basic Implementation of the following n-dimensional Quadratic Function:
f(x) = \frac{1}{2} x^TAx -b^Tx+c
where x,b \in \Bbb R^n and A \in \Bbb R^n \times\Bbb R^n
"""

import numpy as np

from Constants import *

dim = 2


def f(x: type_x, A: type_A, b: type_b, c: type_c):
    return 0.5 * x.T * A * x - b.T * x + c


if __name__ == "__main__":
    y = f(x, A, b, c)
    pass
