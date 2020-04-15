from random import randint
A=[randint (0,100) for i in range (10)]
print (A)

N=10

for i in range(N-1):
    nMin = i
    for j in range(i+1,N):
        if A[j] < A[nMin]:
            nMin = j
    if i!= nMin:
        A[i], A[nMin] = A[nMin], A[i]
print (A)
