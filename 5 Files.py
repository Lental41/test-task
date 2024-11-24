'''
5. Работа с файлами

Написать скрипт, который принимает в качестве параметра командной строки путь к директории и в результате работы 
- рекурсивно обходит заданную директорию, 
- находит все файлы с расширением `*.py`
- выдает в стандартный вывод 
    - суммарное количество строк в найденных файлах `*.py`
    - суммарное количество строк с комментариями в найденных файлах `*.py`
    - количество найденных обращений к команде `import` в найденных файлах `*.py`
'''

import os

def analyze(directory):
    lines_count = 0
    comments_count = 0
    imports_count = 0
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                lines_count += len(lines)
                for line in lines:
                        if "#" in line:
                            comments_count += 1
                        elif line.startswith("import"):
                            imports_count += 1
    print('Строк кода:', lines_count)
    print('Строк с комментариями:', comments_count)
    print('Количество обращений к import:', imports_count)

analyze(r'C:\Users\Pavel\Documents\000\code\test task')