import numpy as np
from math import sqrt

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a matrix A.
    A must be a symmetric, positive-definite matrix.
    
    Returns the lower triangular matrix L such that A = L * L^T.
    """
    n = len(A)
    L = np.zeros((n, n))  # Initialize L with zeros

    for k in range(n):
        # Calculate the diagonal element L[k][k]
        sum_squares = sum(L[k][j] ** 2 for j in range(k))
        L[k][k] = sqrt(A[k][k] - sum_squares)

        # Calculate the off-diagonal elements L[i][k]
        for i in range(k + 1, n):
            sum_products = sum(L[i][j] * L[k][j] for j in range(k))
            L[i][k] = (A[i][k] - sum_products) / L[k][k]

    return L
