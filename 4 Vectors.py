'''
4. ООП

Напишите класс, представляющий объекты типа "трехмерный вектор". 

По заданным трем координатам должен создаваться объект, представляющий вектор и поддерживающий следующие операции:
- сложение вычитание векторов
- умножение и деление вектора на число
- скалярное умножение векторов
- определение длины вектора

Пример возможного использования класса:
a = MyVector(1,2,3)
b = MyVector(3,2,1)

print(a + b)
print(2*a + 3*b)
print(a*b)
print(len(a))
print(len(b))
'''

import math


class vector:
    
    def __init__(self, x, y, z): # конструктор
        self.x = x
        self.y = y
        self.z = z

    def __str__(self):
        return f"Вектор({self.x};{self.y};{self.z})" # перегрузка функции print для вывода вектора

    def __add__(self, other):
        return vector(self.x + other.x, self.y + other.y, self.z + other.z) # перегрузка функции + для сложения векторов
    
    def __sub__(self, other):
        return vector(self.x - other.x, self.y - other.y, self.z + other.z) # перегрузка функции - для вычитания векторов
    
    def __mul__(self, other):
        if isinstance(other, (int, float)):
            return vector(self.x * other, self.y * other, self.z * other) # перегрузка функции * для умножения вектора на число
        if isinstance(other, vector):
            return (self.x * other.x + self.y * other.y + self.z * other.z) # перегрузка функции * для умножения векторов
    
    def __truediv__(self, num):
        return vector(self.x / num, self.y / num, self.z / num) # перегрузка функции / для деления вектора на число
    
    def len(self):
        return (math.sqrt(self.x * self.x + self.y * self.y + self.z * self.z)) # метод, вычисляющий длину вектора


# пример использования
a = vector(3,4,0)
b = vector(8,6,2)

print(a + b)
print(a*2 + b*3)
print(a*b)
print(a.len())
print(b.len())