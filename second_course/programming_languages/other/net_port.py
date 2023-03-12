import socket

print(f'Первое: {socket.getservbyport(80)}\n')
print(f'Второе: {socket.getservbyport(21)}\n')
print("Третье: "+ socket.getservbyport(53, 'udp'), "\n")
print("Четвёртное: " + str(socket.getservbyname('http')))