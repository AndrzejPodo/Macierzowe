import numpy as np
from numpy.lib.function_base import copy


def gaussElimination(arr):
    A = np.array(arr, copy=True)
    n = A.shape[0]
    for k in range(0, n):
        A[k+1:n, k] = A[k+1:n, k]/A[k, k]
        for j in range(k+1, n):
            A[k+1:n, j] -= A[k+1:n, k] * A[k, j]

    return A

def gauss_with_pivoting(arr, u=0.1):
    A = np.array(arr, copy=True)
    n = A.shape[0]
    for k in range(n):
        m = max([abs(x) for x in A[k:n,k]])
        m = u*m
        j_m = k
        for j in range(k,n):
            if abs(A[j, k]) >= m:
                j_m = j
            
        if abs(A[j_m, k]) == 0:
            raise 'macierz osobliwa'
        temp = np.zeros(n-k)
        if j_m != k:
            temp = np.array(A[k, k:n], copy=True)
            A[k, k:n] = np.array(A[j_m, k:n], copy=True)
            A[j_m, k:n] = np.array(temp, copy=True)

        A[k+1:n, k] = A[k+1:n, k]/A[k, k]
        for j in range(k+1, n):
            A[k+1:n, j] -= (A[k+1:n, k] * A[k, j])

    return A

# A = np.random.rand(3, 3)
# print(A)

A = np.array([[0., 4., 1.], [1., 1., 3.], [2., -2., 1.]])
print(A)
A = gauss_with_pivoting(A) 
print(A)
