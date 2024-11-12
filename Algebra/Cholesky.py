import numpy as np
from math import sqrt

def is_symmetric(A):
    """Check if a matrix A is symmetric."""
    return np.allclose(A, A.T)

def is_positive_definite(A):
    """Check if a matrix A is positive definite by testing eigenvalues."""
    return np.all(np.linalg.eigvals(A) > 0)

def cholesky_decomposition(A):
    """
    Perform Cholesky decomposition on a symmetric, positive-definite matrix A.
    
    Parameters:
        A (ndarray): Symmetric, positive-definite matrix of size (n, n).
    
    Returns:
        ndarray: Lower triangular matrix L such that A = L * L.T.
    """
    # Validate the input matrix
    if not is_symmetric(A):
        raise ValueError("Matrix must be symmetric.")
    if not is_positive_definite(A):
        raise ValueError("Matrix must be positive-definite.")

    n = len(A)
    L = np.zeros((n, n))  # Initialize L with zeros

    # Perform Cholesky decomposition
    for k in range(n):
        # Calculate the diagonal element L[k][k]
        sum_squares = sum(L[k][j] ** 2 for j in range(k))
        L[k][k] = sqrt(A[k][k] - sum_squares)

        # Calculate the off-diagonal elements L[i][k]
        for i in range(k + 1, n):
            sum_products = sum(L[i][j] * L[k][j] for j in range(k))
            L[i][k] = (A[i][k] - sum_products) / L[k][k]

    return L

# Example usage
if __name__ == "__main__":
    A = np.array([
        [4, 12, -16],
        [12, 37, -43],
        [-16, -43, 98]
    ])

    try:
        L = cholesky_decomposition(A)
        print("Cholesky Decomposition (Lower triangular matrix L):")
        print(L)
    except ValueError as e:
        print(f"Error: {e}")
