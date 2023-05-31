import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
UDP_IP = '127.0.0.1'
UDP_PORT = 5023
print('Старт сервера на адресе', (UDP_IP,UDP_PORT))
sock.bind((UDP_IP,UDP_PORT))
while True:
    data, client_address = sock.recvfrom(4096)
    if not data or data.decode() == "break":
        break
    try:
        result = socket.getservbyport(int(data.decode()))
    except Exception as e:
        result = "Произошла ошибка: {}".format(e)
    sock.sendto(result.encode(), client_address)
    continue