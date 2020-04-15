import random
def qSort ( A ):
    if len(A) <= 1: return A
    X = random.choice(A) 
    B1 = [ b for b in A if b < X ] 
    BX = [ b for b in A if b == X ] 
    B2 = [ b for b in A if b > X ]
    return qSort(B1)+BX+qSort(B2)
from random import randint
B=[randint (0,100) for i in range (10)]
print(B)
print(qSort(B))

