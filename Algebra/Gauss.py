from numpy import zeros,array, eye, copy, dot

def Gauss(A,b):
    size = len(A)
    A = array(A)
    P = eye(size) 
    for i in range(size-1):
        maxRow = i
        for j in range(i+1,size):
            if abs(A[j][i]) > abs(A[maxRow][i]):
                maxRow = j
        if maxRow != i:
            #### Swap
            P[[maxRow,i]] = P[[i, maxRow]]
            A[[maxRow,i]] = A[[i, maxRow]]
        for k in range(i+1, size):
            A[k][i] /= A[i][i]
            for j in range(i+1, size):
                A[k][j] -= A[k][i]*A[i][j]

    L = eye(size)
    for i in range(size):
        for j in range(i):
            L[i][j] = A[i][j]

    U = zeros((size,size))
    for i in range(size):
        for j in range(i,size):
            U[i][j] = A[i][j]

    b = array(b)

    y = copy(dot(P,b))

    # forwards
    for i in range(size):
        if L[i][i] == 0: #Division by 0
            y[i] = 0
            continue
        for j in range(i):
            y[i] = (y[i] - L[i][j]*y[j])/L[i][i]

    
    x = zeros((size,1))
    x[size-1] = y[size-1]/U[size-1][size-1]

    for i in range(size-1,-1,-1):
        if U[i][i] == 0: #Division by 0
            x[i] = 0
            continue
        xv = y[i]
        for j in range(i+1,size):
            xv -= U[i][j]*x[j]
        xv /= U[i][i]
        x[i] = xv

    return x