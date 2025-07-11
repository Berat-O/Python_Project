import numpy as np
from math import sqrt

def cholesky_decomposition(A: np.ndarray) -> np.ndarray:
    """
    Perform Cholesky decomposition on a matrix A.
    A must be a symmetric, positive-definite matrix.
    
    Returns the lower triangular matrix L such that A = L * L^T.
    
    Raises:
        ValueError: If the input matrix is not square, not symmetric, 
                    or not positive definite.
    """
    # Validate input matrix
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Input matrix must be square")
    
    n = A.shape[0]
    L = np.zeros_like(A, dtype=float)  # Initialize L with zeros
    
    # Check matrix symmetry
    if not np.allclose(A, A.T, atol=1e-10):
        raise ValueError("Input matrix must be symmetric")
    
    for k in range(n):
        # Calculate diagonal element
        diagonal_term = A[k, k] - np.sum(L[k, :k] ** 2)
        
        # Check positive definiteness
        if diagonal_term <= 0:
            raise ValueError("Matrix is not positive definite")
            
        L[k, k] = sqrt(diagonal_term)
        
        # Calculate off-diagonal elements for row k
        for i in range(k + 1, n):
            L[i, k] = (A[i, k] - np.sum(L[i, :k] * L[k, :k])) / L[k, k]
    
    return L
