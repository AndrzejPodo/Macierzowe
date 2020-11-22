import numpy as np

def rank_one_update(C, A, B):
    for i in range(len(C)):
        C[i] += A[i]*B         
    return C

def mul(A, B):
    (m, k1) = A.shape
    (k2, n) = B.shape
    if k1 is not k2:
        raise "bad size of arrays"
    k = k1
    C = np.zeros((m, n))
    for p in range(k):
        for j in range(n):
            C[0:m, j] = rank_one_update(C[0:m, j], A[0:m, p], B[p, j])
    
    return C

A = np.array([3,2,3,2,7,8,1,2,3]).reshape(3,3)
B = np.array([3,2,3,2,7,8]).reshape(3,2)

print(A@B)

print(mul(A,B))
