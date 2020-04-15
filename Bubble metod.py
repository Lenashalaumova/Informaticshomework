from random import randint
A=[randint (0,100) for i in range (10)]
print (A)

N=10

for i in range(N):
    for j in range(N-i-1):
        if A[j+1] < A[j]:
            A[j], A[j+1] = A[j+1], A[j]
print (A)