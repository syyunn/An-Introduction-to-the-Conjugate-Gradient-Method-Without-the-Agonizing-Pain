"""
Basic Implementation of the following n-dimensional Quadratic Function:
f(x) = \frac{1}{2} x^TAx -b^Tx+c
where x,b \in \Bbb R^n and A \in \Bbb R^n \times\Bbb R^n
"""

import numpy as np

from nptyping import Array

dim = 2


def f(x: Array[float, dim, 1],
      A: Array[float, dim, dim],
      b: Array[float, dim, 1],
      c: float):
    return 0.5 * x.T * A * x - b.T * x + c


if __name__ == "__main__":
    x = np.mat([[-6.0], [-6.0]])
    A = np.mat([[3.0, 2.0], [2.0, 6.0]])
    b = np.mat([[2.0], [-8.0]])
    c = 0.0
    y = f(x, A, b, c)
    pass
