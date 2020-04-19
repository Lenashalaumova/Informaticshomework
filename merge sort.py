# метод сортировки: 34 45.56 23 / 1 90.2 7, 34 45 23 56/1 90 2 7, 23 34 45 56/1 2 7 90, 1 2 3 23 34 45 56 90
from random import randint
B=[randint (0,100) for i in range (10)]
print (B)
def merge_sort (B):
    if  len(B) <= 1:
        return B
    middle =int(len(B)/2)
    left=merge_sort(B[:middle])
    right=merge_sort(B[middle:])
    return merge(left,right)
def merge(left,right):
    resurt = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            result.append(left[0])
            left=left[1:]
        else:
            result.append(right[0])
            right = right[1:]
    if len(left) > 0:
        result += left
    if len(right) > 0:
        result += right
    return result
A = merge_sort(B)
print(A)


