# Задать массив случайным образом и отсортировать его по убыванию суммы цифр
from random import randint

def calculateSum(n):
    sum = 0
    while(n):
        sum += n % 10
        n //= 10
    return sum 


a = [randint (0, 100) for i in range (10)]
print('Исходный массив', a)

a = sorted(a, reverse = True, key=calculateSum)
print('Отсортированный массив', a)




