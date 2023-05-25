import os
import socket

SOCKET_FILE = './echo.socket' # путь до сокета
if os.path.exists(SOCKET_FILE): # проверяем существует ли уже этот сокет
    os.remove(SOCKET_FILE) # если да - удаляем его
server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) # создаем сервер с помощью UNIX и TCP(Stream) сокетов
print("Открываем UNIX сокет...")
server.bind(SOCKET_FILE) # биндим сервер по адресу (путь сокета)
server.listen(5) # максимальное количество запросов (не точно)
print("Сервер настроен на прослушивание...") 
while True: # бесконечный цикл 
    try:
        conn, _ = server.accept() # соединяемся с сокетом
        print('Соединение установлено.') 
        while True: # бесконечный цикл
            service = conn.recv(1024).decode() # получаем сервис от клиента
            if not service: # если нет сервиса
                print('Соединение разорвано.')
                break # выходим из вложенного while в верхний
            try: # находим порт сервиса
                port = socket.getservbyname(service) # получаем порт сервиса
                conn.send(("Порт - {} | Сервис - {}".format(port,service)).encode()) # отправляем порт сервиса клиенту
            except Exception as e: # ловим ошибку, если сервиса с таким именем нет
                conn.send(("Произошла ошибка: {}".format(e)).encode()) # отправляем сообщение об ошибке
            continue # продолжаем выполнение с начала в теле while
    except KeyboardInterrupt:
        print('\nВыключение сервера')
        exit(1)