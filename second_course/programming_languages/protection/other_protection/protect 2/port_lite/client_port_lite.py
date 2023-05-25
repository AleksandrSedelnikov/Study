import os
import socket

SOCKET_FILE = './echo.socket' # путь до сокета
print("Подключение...")
if not os.path.exists(SOCKET_FILE): # проверяем, существует ли сокет по адресу SOCKET_FILE
    print('Connection reset.') # если нет
    exit(1) # выход из программы
client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) # создаём клиент на базе UNIX и TCP(Stream) сокетов
client.connect(SOCKET_FILE) # соединяемся с сервером по адресу (путь к сокету)
print('Соединение установлено успешно.')
while True: # бесконечный цикл
    try:
        service = input('Введите название сервиса, порт которого Вы хотите узнать: ') # вводим название сервиса
        client.send(service.encode()) # отправляем название сервиса на сервер (закодировав)
        result = client.recv(1024).decode() # принимаем обратные данные и декодируем их
        print(result) # выводим полученные данные
        continue # начинаем с первой строчки тела while
    except KeyboardInterrupt:
        print('\nВыключение клиента')
        exit(1)