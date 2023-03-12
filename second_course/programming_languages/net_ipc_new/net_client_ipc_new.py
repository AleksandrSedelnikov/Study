#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# изменено: 12.03.2023

import os
import socket
import datetime

# основная функция клиентской части
def main():
    SOCKET_FILE = './echo.socket'
    print("[Client-Info]: Подключение...")
    if not os.path.exists(SOCKET_FILE):
        print('[Client-Info]: Connection reset.')
        exit(1)
    client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    client.connect(SOCKET_FILE)
    print('[Client-Info]: Соединение установлено успешно.')
    print('Для разрыва соединения с сервером можно воспользоваться следующими способами:\n(1) Сочетание Ctrl + C\n(2) Написать break любым способом в терминал\n\nЧтобы выключить сервер через клиент необходимо ввести: serv off\n\n')
    while True:
        try: 
            x = input("Начните ввод запроса > ")
            if (x.upper() == 'BREAK'):
                print('\n[Client-Info]: Выключение клиентской части...')
                exit(1)
            try:
                if (len(x) == 0):
                    print('Вы не указали сообщение, сообщение ретранслируется обратно...')
                    continue
                client.send(x.encode('utf-8'))
            except BrokenPipeError:
                print('\n[Client-Info]: Сервер разорвал соединение...')
                exit(1)
            date_send = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            print('= = =\nОтправлено: {}\nВремя отправления: {}\n= = ='.format(x, date_send))
            response = client.recv(1024).decode()
            if not response:
                print('\n[Client-Info]: Сервер разорвал соединение...')
                exit(1)
            date_input = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            print('= = =\nПолучено: {}\nВремя получения: {}\n= = ='.format(response, date_input))
            
        except KeyboardInterrupt:
            print('\n[Client-Info]: Выключение клиентской части...')
            client.close()
            break
    return 0

if __name__ == "__main__":
    main()    
    