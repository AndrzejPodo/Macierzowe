#zadanie 1
# CSC * wektor
# mul(matix_csc, vec):
# 	result_vec = nowy wektor zer od długości tej samej co vec
# 	 for i = 1..n
# 		for j = COLPTR[I]:(COLPTR[I+1]-1):
# 			result[IRN[j]] += val[j]*vec[i]

# program 3
def coo_to_csr(coo, n):
    nnz = len(coo)
    sorted_coo = sorted(coo) #domyslnie po pierwszym kluczy

    c = 0
    col_ptr = [1]
    for i in range(1, n + 1):
        for (row, _, _) in sorted_coo:
            if row == i:
                c += 1
        col_ptr += [col_ptr[-1] + c]
        c = 0
    
    return [(a,b) for _,a,b in sorted_coo], col_ptr
    

input = [(1, 1, 1), (3, 1, 4), (2, 2, 2), (2, 3, 3), (3, 3, 5)]

print(coo_to_csr(input, 3))