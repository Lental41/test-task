'''
10.
Получить со стандартного ввода три целых положительных числа: a,b,c.
Вывести на стандартный вывод сначала наибольшее, потом наименьшее, потом оставшееся.
Для решения задачи разрешается использовать только операции сравнения и арифметические операции.
Нельзя использовать операции условного перехода (if, switch), стандартные функции (min, max), любые структуры данных (массивы, классы, строки и т.п).
'''

import random

a = int(input())
b = int(input())
c = int(input())

min = 0
max = 0
mid = 0


# первый способ решения перебирает все возможные варианты через условия циклов while и печатает только при подходящем
while a>b and a>c: # проверки на наибольшее число
    print(a)
    break
while b>a and b>c:
    print(b)
    break
while c>b and c>a:
    print(c)
    break
while a<b and a<c: # проверки на наименьшее число
    print(a)
    break
while b<c and b<a:
    print(b)
    break
while c<a and c<b:
    print(c)
    break
while a>b and a<c or (a>c and a<b): # проверки на среднее число
    print(a)
    break
while b>a and b<c or (b>c and b<a):
    print(b)
    break
while c>b and c<a or (c>a and c<b):
    print(c)
    break


# второй способ решения использует рандом для выбора подходящей комбинации путем перебора в цикле
while (max>min and max>mid and min<max and min<mid and mid<max and mid>min) == False:
    max = random.choice([a, b, c])
    min = random.choice([a, b, c])
    mid = random.choice([a, b, c])

print(max, min, mid)


# третий способ решения использует умножение на логические выражения, т.к. true - 1, a false - 0, то при умножении на логически ложное выражение произведение ббудет равно 0
sum = a + b + c
max = (a * (a >= b) * (a >= c) + b * (b > a) * (b >= c) + c * (c > a) * (c > b)) 
min = (a * (a <= b) * (a <= c) + b * (b < a) * (b <= c) + c * (c < a) * (c < b))
mid = sum - max - min # среднее число можно получить, вычтя из суммы всех трех чисел наибольшее и наименьшее

print(max, min, mid)