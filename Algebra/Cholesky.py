from math import sqrt
from numpy import array

def Cholesky(A):
    L = [[0.0 for x in range(len(A))] for y in range(len(A))]
    L = array(L)

    for k in range(len(A)):
        for i in range(len(A)):
            if k is not i:
                L[k][i] += A[k][i]
                for j in range(i-1):
                    L[k][i] -= L[i][j]*L[k][j]
                if L[i][i] == 0:
                    L[k][i] = 0
                else:
                    L[k][i] /= L[i][i]
            else:
                L[k][k] += A[k][k]
                for j in range(k-1):
                    L[k][k] -= pow(L[k][j], 2)
                L[k][k] = sqrt(L[k][k])

    return L