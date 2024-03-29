#!/usr/bin/env python3

import socket
TCP_IP = '127.0.0.1'
TCP_PORT = 5022
BUFFER_SIZE = 1024
MESSAGE = "Hello, World!"
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
s.connect((TCP_IP, TCP_PORT)) 
s.send(MESSAGE.encode('utf-8'))
data = s.recv(BUFFER_SIZE)
s.close()
print("received data: ",data.decode('utf-8'))