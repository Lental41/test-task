'''
2. Минимальная двоичная куча

- Написать функцию, получающую на вход массив из n чисел, и выдающую на выходе массив из тех же элементов, но переупорядоченный таким образом, чтобы удовлетворять свойству минимальной двоичной кучи (сортирующего дерева)
- Сравнить скорость работы предложенной реализации с функцией создания двоичной кучи из встроенного модуля heapq
'''
import heapq
import random
import time

def min_heap(array, n, i):
    min = i                 # определяем индекс текущего родителя, как индекс наименьшего числа
    left_child = 2 * i + 1  # вычисляем индекс левого ребенка
    right_child = 2 * i + 2 # вычисляем индекс правого ребенка
    if left_child < n and array[left_child] < array[min]:
        min = left_child
    if right_child < n and array[right_child] < array[min]:
        min = right_child
    if min != i: # если родитель меньше ребенка, то меняем местами
        array[i], array[min] = array[min], array[i]
        min_heap(array, n, min) # проверяем поддерево ребенка

def make_heap(array):
    n = len(array)
    for i in range(n // 2 - 1, -1, -1): # начинаем сортировку с последнего родителя
        min_heap(array, n, i)
    return array


# сравнение скорости работы созданной функции с heap.heapify
arr = random.sample(range(1, 1000000), 100000)  # создаем массив из 100 000 случайных чисел

start_time = time.time() # измерение времени работы собственной реализации
arr_copy_1 = arr.copy()
make_heap(arr_copy_1)
end_time = time.time()
print(f"Время выполнения собственной реализации: {end_time - start_time} секунд.")

start_time = time.time() # Измерение времени работы heapq.heapify
arr_copy_2 = arr.copy()
heapq.heapify(arr_copy_2)
end_time = time.time()
print(f"Время выполнения heapq.heapify: {end_time - start_time} секунд.")