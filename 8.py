"""
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
"""

import os

folder = input()

def main():
    snr_data = {} # создаем список для хранения последних записей, где ключами будут SNR, а значениями - данные(Frames, F_ers, B_ers, FER, BER)
    for filename in os.listdir(folder):
        if filename.endswith(".txt"):  # обход текстовых файлов в директории
            with open(os.path.join(folder, filename), 'r') as file:
                lines = file.readlines()
                last_record = {} # парсинг файла построчно
                for line in lines:
                    parts = line.split() # разбиваем строку
                    snr = float(parts[0])
                    frames = int(parts[1])
                    f_ers = int(parts[2])
                    b_ers = int(parts[3])
                    fer = float(parts[4])
                    ber = float(parts[5])
                    last_record[snr] = (frames, f_ers, b_ers, fer, ber) # обновляем последнюю запись для данного SNR
                for snr, data in last_record.items(): # добавляем последние записи в словарь
                    snr_data[snr] = data
    return snr_data

snr_data = main()
result_data = [[snr, *data] for snr, data in sorted(snr_data.items())] # создание таблицы для вывода
header = ["SNR", "Frames", "F_ers", "B_ers", "FER", "BER"] # создание заголовка для вывода
print(f"{' '.join(header):<100}")

for row in result_data:
    formatted_row = [f"{val:<10}" if isinstance(val, int) else f"{val:<10.3e}" for val in row] # форматирование каждого значения в строках данных перед выводом
    print(f"{' '.join(formatted_row):<100}")