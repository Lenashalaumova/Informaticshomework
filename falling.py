# Задать массив случайным образом и отсортировать его по убыванию суммы цифр
from random import randint

def calculateSum(n):
    sum = 0
    while(n):
        sum += n % 10
        n //= 10
    return sum  

def bubbleSort(array):
    arrayMaxIdx = len(array) - 1
    for i in range(arrayMaxIdx):
        for j in range(arrayMaxIdx - i):
            if calculateSum(array[j+1]) > calculateSum(array[j]):
                array[j], array[j+1] = array[j+1], array[j]


a = [randint (0, 100) for i in range (10)]
print('Исходный массив', a)

bubbleSort(a)
print('Отсортированный массив', a)




