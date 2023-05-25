import socket
            
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP = '127.0.0.1'
UDP_PORT = 5023
server_address = (UDP_IP,UDP_PORT)
print('Старт сервера на адресе', server_address)
sock.bind(server_address)
while True:
    data, client_address = sock.recvfrom(4096)
    if not data or str(data.decode()) == 'break':
        exit(1)
    try:
        result = socket.gethostbyname(data.decode())
    except Exception as e:
        result = "Произошла ошибка: {}".format(e)
    sock.sendto(result.encode(), client_address)
    continue
