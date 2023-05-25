#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
users = subprocess.check_output("who | awk '{print $1}' | sort -u", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
buff = open('buffer.txt','w')
buff.write(users)
buff.close()
buff = open('buffer.txt','r')
users = buff.readlines()
buff.close()
print("<h1>Пользователи онлайн:</h1>\n")
for i in users:
    print("<h2>Привет, {}</h2>\n".format(i[:-1]))