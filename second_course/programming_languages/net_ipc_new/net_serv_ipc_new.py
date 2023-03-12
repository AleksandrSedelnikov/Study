#! /usr/bin/env python3
# -*- coding: utf-8 -*-
# изменено: 12.03.2023

global connection_count
global message_count
import os
import socket
import datetime

# функция получения/разрыва соединения с клиентской частью
def connection(server):
    global connection_count
    global message_count
    connection_count = 1
    while True:
        conn, _ = server.accept()
        print('= = =\n[Server-Info]: Получено соединение [ID {}]\n= = ='.format(connection_count))
        start_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        message_count = 0
        result = message_response(conn)
        if (result == 0):
            return 0
        elif (result == 1):
            print('= = =\n[Server-Info]:\nСоединение [ID {}] разорвано'.format(connection_count))
            date_format = "%d.%m.%Y %H:%M:%S"
            reset_time = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            buff_time_start = datetime.datetime.strptime(start_time, date_format)
            buff_time_reset = datetime.datetime.strptime(reset_time, date_format)
            delta = buff_time_reset - buff_time_start
            print('Время соединения: {} дней, {} часов, {} минут, {} секунд.\n= = ='.format(delta.days, delta.seconds // 3600, (delta.seconds // 60) % 60, delta.seconds))
        connection_count += 1

# функция обработки и отправки сообщения
def message_response(connect):
    global connection_count
    global message_count
    while True:
        response = connect.recv(1024).decode()
        if not response:
            return 1
        if (response.lower() == "serv off"):
            return 0
        message_count += 1
        if (str(response).lower() == "debug"):
            msg = '\n[Debug-Info]\nНомер соединения: {}\nКоличество сообщений за соединение: {}'.format(connection_count, message_count)
            connect.send(msg.encode())
            print('= = =\n[Server-Info]: ВНИМАНИЕ! Была отправлена техническая информация\n= = =')
            continue
        date_input = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print('= = =\nПолучено: {}\nВремя получения: {}\n= = ='.format(response, date_input)) 
        msg = input('Начните ввод ответа > ')
        if (len(msg) == 0):
            print('= = =\n[Server-Error]: Empty response\n= = =')
            connect.send('К сожалению, сервер не указал ниодного символа в сообщении, повторите запрос...'.encode())
            continue
        try:
            connect.send(msg.encode())
        except Exception:
            print('= = =\n[Server-Info]: Соединение с клиентской частью было разорвано...\n= = =')
            continue
        date_send = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        print('= = =Отправлено: {}\nВремя ответа: {}\n= = ='.format(msg, date_send)) 

# основная функция серверной части
def main():
    SOCKET_FILE = './echo.socket'
    if os.path.exists(SOCKET_FILE):
        os.remove(SOCKET_FILE)

    with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as server:
        print("= = =\n[Server-Info]: Открываем UNIX сокет...")
        server.bind(SOCKET_FILE)
        server.listen(5)
        print("[Server-Info]: Сервер настроен на прослушивание...\n= = =")    
        try:
            if (connection(server) == 0):
                server.close()
                os.remove(SOCKET_FILE)
                print('= = =\n[Server-Info]: Сервер выключен...\n= = =')
                exit(1)
        except KeyboardInterrupt:
            server.close()
            os.remove(SOCKET_FILE)
            print("= = =\n[Server-Info]: Сервер выключен...\n= = =")
        return 0

if __name__ == "__main__":
    main()
