import socket

def client(sock, server_address):
    """
    param:\n
    sock - socket.socket(socket.*, socket.*)\n
    server_address - sock file path
    """
    print('Приветствую, милорд!\nЧтобы узнать деление числа, достаточно ввести число после "Введите число > "\nЕсли Вы устанете и захотите покинуть сие место, нажмите Ctrl+C или введите что-то из: bb,bye,good bye,break.\nУспехов, милорд!')
    while True:
        try:
            number = input('Введите число > ')
            if (number in ['bb', 'bye', 'good bye', 'break']):
                print('Всего доброго, милорд!')
                return 0
            sock.sendto(number.encode(), server_address)
            result, _ = sock.recvfrom(4096)
            print(result.decode())
        except KeyboardInterrupt:
            print('\nВсего доброго, милорд!')
            return 0

def main():
    sock = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
    server_address = 'server.sock'
    sock.bind("")
    result = client(sock=sock, server_address=server_address)
    if result == 0:
        exit(1)

if __name__ == "__main__":
    main()

