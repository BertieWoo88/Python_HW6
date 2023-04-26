'''
Задача 32: Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

'''

from random import randint

n = int(input('введите размерность списка: '))

listA = [randint(-10, 10) for i in range(n) ]

print(listA)

a = int(input('введите минимум: '))
b = int(input('введите максимум: '))


def findIndexRang(listcheck, lMin, lMax):
    listRes = []
    for i in range(len(listcheck)):
        if lMin<=listcheck[i]<=lMax:
            listRes.append(i)
    return listRes


print(findIndexRang(listA, a, b))
