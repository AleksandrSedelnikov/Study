import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5023
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Открываем INET сокет...")
server.bind((TCP_IP, TCP_PORT))
server.listen(5)
print("Сервер настроен на прослушивание...")
while True:
    connect, addr = server.accept()
    print('Получено соединение [IP {} | PORT {}]'.format(addr[0], addr[1]))
    BUFFER_SIZE = 4096
    while True:
        data = connect.recv(BUFFER_SIZE).decode('utf-8')
        if not data:
            print('Сервер выключен')
            exit(1)
        data = data.split(" ")
        result = float(data[0]) * float(data[1])
        connect.send(str(result).encode())
        continue