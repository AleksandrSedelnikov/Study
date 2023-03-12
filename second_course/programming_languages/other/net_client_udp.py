#!/usr/bin/env python3

import socket
UDP_IP = "127.0.0.1"
UDP_PORT = 5022
MESSAGE = "Hello, World!"
print("UDP target IP: {}".format(UDP_IP))
print("UDP target port: {}".format(UDP_PORT))
print("message: {}".format(MESSAGE))
sock = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
sock.sendto (MESSAGE.encode('utf-8'), (UDP_IP, UDP_PORT))