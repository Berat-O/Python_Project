import numpy as np

def gaussian_elimination_with_pivoting(A, b):
    """Perform Gaussian elimination with partial pivoting on matrix A and vector b."""
    size = len(A)
    A = np.array(A, dtype=float)  # Ensure A is a float array
    b = np.array(b, dtype=float)  # Ensure b is a float array
    P = np.eye(size)  # Initialize the permutation matrix

    # Partial Pivoting and Elimination
    for i in range(size - 1):
        # Find the pivot row
        max_row = max(range(i, size), key=lambda k: abs(A[k][i]))
        if max_row != i:
            # Swap rows in both A and P for pivoting
            A[[i, max_row]] = A[[max_row, i]]
            P[[i, max_row]] = P[[max_row, i]]
            b[i], b[max_row] = b[max_row], b[i]  # Also swap entries in b

        # Perform elimination
        for k in range(i + 1, size):
            factor = A[k][i] / A[i][i]
            A[k, i:] -= factor * A[i, i:]  # Update only remaining elements in row
            b[k] -= factor * b[i]          # Update b vector accordingly

    # Extract L and U matrices from A
    L = np.eye(size)
    U = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            if i > j:
                L[i][j] = A[i][j]
            else:
                U[i][j] = A[i][j]

    return P, L, U, b

def forward_substitution(L, Pb):
    """Solve the equation Ly = Pb using forward substitution."""
    size = len(L)
    y = np.zeros(size)
    for i in range(size):
        y[i] = (Pb[i] - np.dot(L[i, :i], y[:i])) / L[i][i]
    return y

def backward_substitution(U, y):
    """Solve the equation Ux = y using backward substitution."""
    size = len(U)
    x = np.zeros(size)
    for i in range(size - 1, -1, -1):
        x[i] = (y[i] - np.dot(U[i, i + 1:], x[i + 1:])) / U[i][i]
    return x

def solve_gaussian(A, b):
    """Main function to solve the system Ax = b using Gaussian elimination with pivoting."""
    # Step 1: Gaussian Elimination with Partial Pivoting to get P, L, U
    P, L, U, Pb = gaussian_elimination_with_pivoting(A, b)

    # Step 2: Forward substitution to solve Ly = Pb
    y = forward_substitution(L, Pb)

    # Step 3: Backward substitution to solve Ux = y
    x = backward_substitution(U, y)

    return x

# Example usage:
A = [[2, -1, 1],
     [3, 3, 9],
     [3, 3, 5]]
b = [2, -1, 4]

x = solve_gaussian(A, b)
print("Solution x:", x)
