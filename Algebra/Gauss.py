import numpy as np

def gauss_elimination(A, b):
    A = np.asarray(A, dtype=float)
    b = np.asarray(b, dtype=float)
    
    if A.ndim != 2 or A.shape[0] != A.shape[1]:
        raise ValueError("Coefficient matrix A must be square")
    
    n = A.shape[0]
    
    if b.ndim != 1 or len(b) != n:
        raise ValueError("Right-hand side vector b must have same length as rows of A")
    
    augmented = np.column_stack((A, b))
    
    for i in range(n):
        max_row = np.argmax(np.abs(augmented[i:, i])) + i
        if max_row != i:
            augmented[[i, max_row]] = augmented[[max_row, i]]
        
        pivot = augmented[i, i]
        if np.abs(pivot) < 1e-10:
            raise ValueError("Matrix is nearly singular, cannot solve using Gaussian elimination")
        
        augmented[i, i:] /= pivot
        
        for j in range(i+1, n):
            factor = augmented[j, i]
            augmented[j, i:] -= factor * augmented[i, i:]
    
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        x[i] = augmented[i, -1] - np.sum(augmented[i, i+1:-1] * x[i+1:])
    
    return x
