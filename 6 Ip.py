'''
6. Многопоточность

Напишите скрипт, реализующий проверку доступности диапазона ip адресов с использованием команды `ping -c5 <ip>` запускаемой в многопоточном режиме.
Скрипт принимает 3 параметра командной строки: адрес подсети вида `192.168.1.0` и диапазон ip адресов вида `100 200`

Пример запуска `python myping.py 192.168.1.0 100 200`

На выходе - строки вида `<IP> -> status`
'''

import subprocess
import sys
import threading

def ping_ip(ip):
    result = subprocess.run(['ping', '-n', '5', ip], stdout=subprocess.PIPE) # функция для выполнения ping
    if result.returncode == 0:
        print(f"{ip} -> reachable")
    else:
        print(f"{ip} -> unreachable")

def main():
    subnet = sys.argv[1] # получаем адрес подсети
    start_range = int(sys.argv[2]) # получаем начало диапазона ip адресов
    end_range = int(sys.argv[3]) # получаем конец диапазона ip адресов    
    ips = []
    for i in range(start_range, end_range + 1): # генерация списка IP-адресов
        ip = subnet.split('.')[0] + '.' + subnet.split('.')[1] + '.' + subnet.split('.')[2] + '.' + str(i)
        ips.append(ip)        
    threads = []
    for ip in ips:
        thread = threading.Thread(target=ping_ip, args=(ip,))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()

main()