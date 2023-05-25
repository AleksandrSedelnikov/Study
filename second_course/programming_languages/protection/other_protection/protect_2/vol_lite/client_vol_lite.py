import socket

TCP_IP = '127.0.0.1'
TCP_PORT = 5023
BUFFER_SIZE = 4096
print("Подключение...")
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
try:
    client.connect((TCP_IP, TCP_PORT)) 
except ConnectionRefusedError:
    print('Connection reset.')
    exit(1)
print('Соединение установлено успешно.')
print('Чтобы выключить клиент и сервер введите break при вводе пик.знач. либо скважности')
while True:
    try:
        vol = str(input('Введите пиковое значение напряжения: '))
        q = str(input('Введите скважность: '))
        message = vol + " " + q
        if q == 'break' or vol == 'break':
            print('Конец работы')
            exit(1)
        try:
            float(vol)
            float(q)
        except:
            print('Введено не число.')
            continue
        client.send(message.encode())
        result = client.recv(BUFFER_SIZE).decode()
        print('Среднее значение напряжения: {}'.format(result))
        continue
    except KeyboardInterrupt:
        print('\nКлиент выключен')
        exit(1)