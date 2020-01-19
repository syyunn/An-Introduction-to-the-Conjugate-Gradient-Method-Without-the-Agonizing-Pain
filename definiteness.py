"""
Code to check the definiteness of given Matrix
"""

from Constants import *


def check_positive_definite(A: type_A):
    """
    A matrix 𝐴 is positive definite if and only if the symmetric matrix
    𝑀=𝐴+𝐴^𝑇 is positive definite.
    """
    M = A + A.T
    # How to check symmetric matrix is positive-definite
    pass


if __name__ == "__main__":
    pass
