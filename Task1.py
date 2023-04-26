'''
Задача 30:  Заполните массив элементами арифметической прогрессии. 
Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
Каждое число вводится с новой строки.
'''
a = int(input('введите стартоваое значение: '))
b = int(input('введите шаг: '))
d = int(input('введите размерность: '))

def aprogress(start, step, length):
    lastnum = start + length*step
    return [i for i in range(start, lastnum, step)]


print(aprogress(a,b, d))

