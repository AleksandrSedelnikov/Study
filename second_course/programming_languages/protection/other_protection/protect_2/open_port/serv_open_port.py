import os
import socket
import subprocess

SOCKET_FILE = './echo.socket'
if os.path.exists(SOCKET_FILE):
    os.remove(SOCKET_FILE)
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
print("Открываем UNIX сокет")
server.bind(SOCKET_FILE)
server.listen(5)
print("Сервер настроен на прослушивание")    
try:
    while True:
        connect, _ = server.accept()
        print('Получено соединение')
        while True:
            response = connect.recv(1024).decode()
            if not response:
                print('Соединение разорвано.')
                continue
            try:
                try:
                    first_check = subprocess.check_output("nmap -sT {} | grep 'open'".format(response),stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
                    second_check = first_check.split()
                    second_check = [i for i in second_check if i != 'open']
                except Exception as e:
                    second_check = 1
                if (second_check == 1):
                    msg = "Неверный IP-адрес"
                else:
                    msg = ""
                    i = 0
                    while i < len(second_check):
                        msg += 'Порт: {} | Сервис: {}\n'.format(second_check[i],second_check[i+1])
                        i += 2
                connect.send(msg.encode())
            except Exception:
                print('Соединение с клиентской частью было разорвано\n')
                continue
            continue
except KeyboardInterrupt:
    server.close()
    os.remove(SOCKET_FILE)
    print('\nСервер выключен')