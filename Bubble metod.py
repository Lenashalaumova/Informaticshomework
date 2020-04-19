#метод пузырька например: 9 2 6 5 4  8
from random import randint
A=[randint (0,100) for i in range (10)]
print (A)

N=10

for i in range(N):
    for j in range(N-i-1): #шаг
        if A[j+1] < A[j]: #если меньше: 2 9 6 5 4 8
            A[j], A[j+1] = A[j+1], A[j] #поменять местами
print (A)
#2 8 6 5 4 9, 2 4 6 5 8 9, 2 4 5 6 8 9