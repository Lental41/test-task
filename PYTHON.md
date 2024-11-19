# Тестовое задание для студента, который любит программировать


Предложите ваши варианты решения для 4 и более заданий и следующего списка


1. Числа Фибоначии

- Напишите функцию, вычисляющую n-е число Фибоначчи. На вход функции поступает число 0<n<35, на выходе n-e число Фибоначии. 
Постарайтесь предложить максимально производительную реализацию функции.
- Напишите функцию, вычисляющую последнюю цифру числа Фибоначчи по заданному n. 


2. Минимальная двоичная куча

- Написать функцию, получающую на вход массив из n чисел, и выдающую на выходе массив из тех же элементов, но переупорядоченный таким образом, чтобы удовлетворять свойству минимальной двоичной кучи (сортирующего дерева)
- Сравнить скорость работы предложенной реализации с функцией создания двоичной кучи из встроенного модуля heapq


3. Расстояние редактирования

*) это минимальное количество вставок, удалений и замен символов, необходимое для преобразования строки A в B. Данное число называется расстоянием редактирования или расстоянием Левенштейна.

- Напишите функцию для вычисления расстояния редактирования двух данных непустых строк содержащих строчные буквы латинского алфавита.


4. ООП

Напишите класс, представляющий объекты типа "трехмерный вектор". 

По заданным трем координатам должен создаваться объект, представляющий вектор и поддерживающий следующие операции:
- сложение вычитание векторов
- умножение и деление вектора на число
- скалярное умножение векторов
- определение длины вектора

Пример возможного использования класса:
```
a = MyVector(1,2,3)
b = MyVector(3,2,1)

print(a + b)
print(2*a + 3*b)
print(a*b)
print(len(a))
print(len(b))
```


5. Работа с файлами

Написать скрипт, который принимает в качестве параметра командной строки путь к директории и в результате работы 
- рекурсивно обходит заданную директорию, 
- находит все файлы с расширением `*.py`
- выдает в стандартный вывод 
    - суммарное количество строк в найденных файлах `*.py`
    - суммарное количество строк с комментариями в найденных файлах `*.py`
    - количество найденных обращений к команде `import` в найденных файлах `*.py`


6. Многопоточность

Напишите скрипт, реализующий проверку доступности диапазона ip адресов с использованием команды `ping -c5 <ip>` запускаемой в многопоточном режиме.
Скрипт принимает 3 параметра командной строки: адрес подсети вида `192.168.1.0` и диапазон ip адресов вида `100 200`

Пример запуска `python myping.py 192.168.1.0 100 200`

На выходе - строки вида `<IP> -> status`


7. Базы данных

- Напишите скрипты для создания базы данных и для добавления информации в базу данных. Используйте встроенный модуль sqlite3. Структура и наполнение базы данных на Ваше усмотрение.
- Добавьте скрипт для вывода информации по какой-нибудь выборке из базы данных.


8.
Есть М текстовых файлов с результатами симуляции некоторого декодера, каждый файл следующей структуры:

'''
# SNR   Frames   F_ers   B_ers     FER       BER
 6.40   12500     16      125    1.280e-3  2.441e-6
 6.40   12600     17      128    1.349e-3  2.480e-6
'''

Размер одного фрейма: frame_size = 4096 бит.
Записей с одинаковым SNR может быть несколько.
Если в одном файле содержатся записи с разными SNR, то они расположены последовательно, по возрастанию SNR.
Для анализа актуальной является только самая последняя запись с каждым значением SNR.
Требуется получить (вывести на стандартный вывод) таблицу, объединяющую собранную статистику по всем M файлам.


9.
Создать класс, реализующий действия с элементами поля Галуа GF(2^m).
Требуемые действия: арифметические действия, возведение в степень, логарифмы, нахождение обратного элемента.


10.
Получить со стандартного ввода три целых положительных числа: a,b,c.
Вывести на стандартный вывод сначала наибольшее, потом наименьшее, потом оставшееся.
Для решения задачи разрешается использовать только операции сравнения и арифметические операции.
Нельзя использовать операции условного перехода (if, switch), стандартные функции (min, max), любые структуры данных (массивы, классы, строки и т.п).
