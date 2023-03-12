import socket
import datetime

# основная функция клиентской части
def main():
    TCP_IP = '127.0.0.1'
    TCP_PORT = 5022 # поменять последние две цифры на номер своего аккаунта (прим: AP103_22 => 22)
    BUFFER_SIZE = 1024
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
            x = input("Начните ввод запроса > ")
            if (x.upper() == 'BREAK'):
                print('\n[Client-Info]: Выключение клиентской части...')
                exit(1)
            if (len(x) == 0):
                print('Вы не указали сообщение, сообщение ретранслируется обратно...')
                continue
            client.send(x.encode('utf-8'))
            date_send = datetime.datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            print('= = =\nОтправлено: {}\nВремя отправления: {}\n= = ='.format(x, date_send))
            response = client.recv(BUFFER_SIZE).decode('utf-8')
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