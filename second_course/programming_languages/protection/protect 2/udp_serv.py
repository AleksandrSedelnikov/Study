import socket
import os

def server(sock):
    """
    param:\n
    sock - socket.socket(socket.*, socket.*)\n
    """
    while True:
        try:
            data, client_address = sock.recvfrom(4096)
            if not data:
                break
            try:
                number = int(data.decode())
            except ValueError:
                result = 'Ответ → Ошибка: полученные данные не являются числом'
                sock.sendto(result.encode(), client_address)
                continue
            result = ''
            count_result = 0
            if number % 3 == 0:
                result += 'Делится на 3. Результат: {}\n'.format(number // 3)
                count_result += 1
            if number % 6 == 0:
                result += 'Делится на 6. Результат: {}\n'.format(number // 6)
                count_result += 1
            if number % 9 == 0:
                result += 'Делится на 9. Результат: {}\n'.format(number // 9)
                count_result += 1
            if result == '':
                result = 'Не делится на 3, 6, 9.'
                count_result += 1
            if count_result == 1:
                result = 'Ответ → ' + result
            else:
                result = 'Ответ ↓\n' + result
            sock.sendto(result.encode(), client_address)
        except KeyboardInterrupt:
            return 0


def main():
    """
    info:\n
    default function
    """
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    try:
        os.remove('server.sock')
    except OSError:
        pass
    server_address = 'server.sock'
    print('Старт сервера на адресе', server_address)
    sock.bind(server_address)
    result = server(sock=sock)
    if result == 0:
        print('\nСервер остановлен.')
        exit(1)

if __name__ == "__main__":
    main()
