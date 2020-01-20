"""
Basic Implementation of the following n-dimensional Quadratic Function:
f(x) = \frac{1}{2} x^TAx -b^Tx+c
where x,b \in \Bbb R^n and A \in \Bbb R^n \times\Bbb R^n
"""

from Constants import *

dim = 2


def f(x: type_x, A: type_A, b: type_b, c: type_c):
    return 1 / 2 * x.T * A * x - b.T * x + c


def f_derivative(x: type_x, A: type_A, b: type_b):
    return 1 / 2 * (A.T * x + A * x) - b
    # Check https://calculus.subwiki.org/wiki/Quadratic_function_of_multiple_variables
    # only in case A is symmetric, this form is reduced to A*x -b


if __name__ == "__main__":
    y = f(x, A, b, c)
    pass
