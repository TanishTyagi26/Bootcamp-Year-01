import numpy as np

A = np.arange(1,101).reshape(10,10)
print(A)

prime_rows = A[[1,2,4,6]]
print(prime_rows)

B = A.copy()
B[:,::2] = B[::-1,::2]
print(B)

C = A.copy()
np.fill_diagonal(C,0)
print(C)


top = A[0,:]
bottom = A[-1,:]
left = A[1:-1,0]
right = A[1:-1,-1]
border_sum = np.sum(top)+np.sum(bottom)+np.sum(left)+np.sum(right)
print( border_sum)


rotated = np.rot90(A,-1)
print(rotated)