'''
7. Базы данных

- Напишите скрипты для создания базы данных и для добавления информации в базу данных. Используйте встроенный модуль sqlite3. Структура и наполнение базы данных на Ваше усмотрение.
- Добавьте скрипт для вывода информации по какой-нибудь выборке из базы данных.
'''

import sqlite3

conn = sqlite3.connect('library.db')
cursor = conn.cursor()

# создание таблицы с книгами
cursor.execute('''
CREATE TABLE books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    author TEXT NOT NULL,
    genre TEXT NOT NULL
)
''')

# добавление данных в таблицу
cursor.execute('''
INSERT INTO books (title, author, genre)
VALUES
    ('Faust', 'Johann Goethe', 'Poem'),
    ('1984', 'George Orwell', 'Dystopian'),
    ('War and Peace', 'Leo Tolstoy', 'Historical novel'),
    ('Guards! Guards!', 'Terry Pratchett', 'Fantasy')
''')

conn.commit()

# выборка книг жанра фэнтези
genre = 'Fantasy'
cursor.execute('''
SELECT id, title, author, genre
FROM books
WHERE genre = ?
''', (genre,))

# Вывод результатов выборки
books = cursor.fetchall()
print(f"Books in genre '{genre}':")
for book in books:
    print(f"ID: {book[0]}, Title: {book[1]}, Author: {book[2]}, Genre: {book[3]}")

conn.close()