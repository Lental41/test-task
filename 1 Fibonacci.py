'''
1. Числа Фибоначии

- Напишите функцию, вычисляющую n-е число Фибоначчи. На вход функции поступает число 0<n<35, на выходе n-e число Фибоначии. 
Постарайтесь предложить максимально производительную реализацию функции.
- Напишите функцию, вычисляющую последнюю цифру числа Фибоначчи по заданному n. 
'''

a = 1
b = 0
n = int(input())
if n > 0 and n < 35:
    for i in range(n-1):
        b = a + b # b - i-e число Фибоначчи
        a = b - a # a - i-1 число Фибоначчи
    print(n, '\b-е число Фибоначчи:', b)
    print('Последняя цифра:', b%10)
else:
    print("Неверное число")