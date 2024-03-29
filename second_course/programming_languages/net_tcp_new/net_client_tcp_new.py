import socket
import datetime

# основная функция клиентской части
def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5022
    BUFFER_SIZE = 4096
    print("[Client-Info]: Подключение...")
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        client.connect((TCP_IP, TCP_PORT)) 
    except ConnectionRefusedError:
        print('[Client-Info]: Connection reset.')
        exit(1)
    print('[Client-Info]: Соединение установлено успешно.')
    print('Для разрыва соединения с сервером можно воспользоваться следующими способами:\n(1) Сочетание Ctrl + C\n(2) Написать break любым способом в терминал\n\nЧтобы выключить сервер через клиент необходимо ввести: serv off\n\n')
    while True:
        try:
            var = input('Выберите тип запроса (GET/POST): ')
            if (var.upper() != 'GET' and var.upper() != 'POST' and var.upper() != 'BREAK'):
                print('Вы ввели неверное название типа запроса.')
                continue 
            if (var.upper() == 'GET'):
                x = input("Начните ввод GET-запроса > ")
                if (x.upper() == 'BREAK'):
                    print('\n[Client-Info]: Выключение клиентской части...')
                    exit(1)
                if (len(x) == 0):
                    print('Вы не указали сообщение, сообщение ретранслируется обратно...')
                    continue
                message = var.upper() + " /myserver/?{} HTTP/1.1 host:localhost:3306".format(x)
                client.send(message.encode('utf-8'))
                response = client.recv(BUFFER_SIZE).decode('utf-8')
                if not response:
                    print('\n[Client-Info]: Сервер разорвал соединение...')
                    exit(1)
                print('= = =\nПолучено: {}\n= = ='.format(response))
                continue

            elif (var.upper() == 'POST'):
                x = input("Начните ввод POST-запроса > ")
                if (x.upper() == 'BREAK'):
                    print('\n[Client-Info]: Выключение клиентской части...')
                    exit(1)
                if (len(x) == 0):
                    print('Вы не указали сообщение, сообщение ретранслируется обратно...')
                    continue
                message = var.upper() + "  /myserver/ HTTP/1.1" + x
                client.send(message.encode('utf-8'))
                date_send = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                print('= = =\nОтправлено: {}\nВремя отправления: {}\n= = ='.format(x, date_send))
                response = client.recv(BUFFER_SIZE).decode('utf-8')
                if not response:
                    print('\n[Client-Info]: Сервер разорвал соединение...')
                    exit(1)
                date_input = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
                print('= = =\nПолучено: {}\nВремя получения: {}\n= = ='.format(response, date_input))
            elif (var.upper() == 'BREAK'):
                print('\n[Client-Info]: Выключение клиентской части...')
                exit(1)
        except KeyboardInterrupt:
            print('\n[Client-Info]: Выключение клиентской части...')
            client.close()
            break
    return 0

if __name__ == "__main__":
    main()    