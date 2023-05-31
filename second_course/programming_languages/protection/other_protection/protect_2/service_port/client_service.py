import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP = '127.0.0.1'
UDP_PORT = 5023
server_address = (UDP_IP,UDP_PORT)
flag = 0
while (flag == 0):
    message = str(input('Введите порт: '))
    if (message.isdigit()):
        sock.sendto(message.encode(), server_address)
        result, _ = sock.recvfrom(4096)
        if (result.decode()).find('Произошла ошибка') == -1:
            print('Название сервиса указанного порта: {}'.format(result.decode()))
        else:
            print(result.decode())
    else:
        print('Вы ввели не цифры')
    check_flag = input('Хотите продолжить?(Введите yes/no): ')
    if (check_flag == "no"):
        flag = 1
        message = 'break'
        sock.sendto(message.encode(), server_address)
        continue
    continue