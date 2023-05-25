import os
import socket

# функция проверки валидности IP
def isValidIP(s):
    if s.count('.') != 3:
        return 0
    l = list(map(str, s.split('.')))
    for ele in l:
        if int(ele) < 0 or int(ele) > 255 or (ele[0]=='0' and len(ele)!=1):
            return 0
    return 1

SOCKET_FILE = './echo.socket'
print("Подключение...")
if not os.path.exists(SOCKET_FILE):
    print('Connection reset.')
    exit(1)
client = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
client.connect(SOCKET_FILE)
print('Соединение установлено успешно.')
while True:
    try: 
        x = input("Начните ввод запроса > ")
        if (x.upper() == 'BREAK'):
            print('\nВыключение клиентской части')
            exit(1)
        else:
            result = isValidIP(x)
            if (result == 0):
                print('неверный ip')
                continue
        try:
            if (len(x) == 0):
                print('Вы не указали сообщение, сообщение ретранслируется обратно...')
                continue
            client.send(x.encode('utf-8'))
        except BrokenPipeError:
            print('\nСервер разорвал соединение')
            exit(1)
        response = client.recv(4096).decode()
        if not response:
            print('\nСервер разорвал соединение')
            exit(1)
        print(response)
        
    except KeyboardInterrupt:
        print('\nВыключение клиентской части')
        client.close()
        break
    