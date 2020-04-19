#быстрая сортировка. Пример: 34 88 23 1 99 44 Выбираем ключевой элемент: пусть будет 88
from random import randint
import random
def qSort ( A ): #88
    if len(A) <= 1: return A
    X = random.choice(A) 
    B1 = [ b for b in A if b < X ] #числа, которые меньше 88 в левую сторону: 1 23 34 44
    BX = [ b for b in A if b == X ] #числа, которые равны 88 остаются рядом с ним: нету
    B2 = [ b for b in A if b > X ] #числа, которые больше 88 в правую сторону:99
    return qSort(B1)+BX+qSort(B2) # меньше + равные и это самое число + больше: 1 23 34 44 + 88 + 99

B=[randint (0,100) for i in range (10)]
print(B)
print(qSort(B)) # 1 23 34  44 88 99

