from random import randint

def isSimple(x):
    for j in range(2, x):
        if x % j == 0:
            return False
    return True

a=[randint (0,100) for x in range (10)]
print (a)
b=[]
for x in a:
    if isSimple(x) and x != 0:
        b.append(x)
print(b)
