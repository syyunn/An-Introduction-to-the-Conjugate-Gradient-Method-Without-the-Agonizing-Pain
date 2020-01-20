"""
Code to check the definiteness of given Matrix
refer to matlab's "chol" function: https://www.mathworks.com/help/matlab/math
/determine-whether-matrix-is-positive-definite.html
"""

from Constants import *

from sympy.matrices import Matrix


def check_symmetry(A: type_A):
    if A.shape[0] == 2:
        if np.asarray(A)[0, 1] == np.asarray(A)[1, 0]:
            return True
        else:
            return False
    pass


def check_positive_definite(A: type_A):
    """
    1. General Method
    Cholesky decomposition will fail only when the matrix is not symmetric positive semi definite. Thus, if the algorithm doesn’t work, then you know your matrix is not symmetric positive semidefinite.
    2. (Assume A is Hermitian)
    "A is positive definite if and only if all of its eigenvalues are
    positive. (keep in mind that eigenvalues' are not required to be
    distinctive to one another)"
    https://en.wikipedia.org/wiki/Definiteness_of_a_matrix#Eigenvalues
    """
    # How to check symmetric matrix is positive-definite
    # Check Gershgorin circle theorem
    symmetry = check_symmetry(A)
    assert symmetry, "positive definite only defined for symmetric matrix"

    if A.shape[0] == 2 :
        M = Matrix(A)
        roots = M.charpoly().all_roots()
        return all(element > 0 for element in roots)
    pass


def decompose_Cholesky():
    """
    The Cholesky decomposition of a Hermitian positive-definite matrix A is a
    decomposition of the form A = LL*, where L is a lower triangular matrix
    with real and positive diagonal entries, and L* denotes the conjugate
    transpose of L
    """


def decompose_Eigen():
    """https://en.wikipedia.org/wiki/Eigendecomposition_of_a_matrix#Real_symmetric_matrices
    Only diagonalizable matrices can be factorized in this way.
    """
    pass


def check_Diagonalizabe():
    """Check whether the matrix is diagonalizable (so that we can proceed to eigen_decomposition)
    (hint1) A matrix is diagonalizable if and only if for each eigenvalue the dimension of the eigenspace is equal to the multiplicity of the eigenvalue.
    """
    pass


if __name__ == "__main__":
    positive_definite = check_positive_definite(A)
    pass
