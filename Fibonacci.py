from random import randint
from math import sqrt


        
def isFib(x):
    if sqrt(5*(x**2)-4)%1 == 0 or sqrt(5*(x**2)+4)%1 == 0:
        return True
    return False

a = [randint(0, 100) for x in range(10)]
print(a)
b = []
for x in a:
    if isFib(x):
        b.append(x)




print(b)
