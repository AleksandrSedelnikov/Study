#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
flag_start = True
flag_end = True
if not "start" in form:
    flag_start = False
else:
    start_port = form.getvalue("start")
if not "end" in form:
    flag_end = False
else:
    end_port = form.getvalue("end")
if (flag_start == True and flag_end == True):
    try:
        int(flag_start)
        int(flag_end)
    except:
        print("<h2>Указан какой-то неверный порт</h2>")
    port_open = subprocess.check_output("nmap -sT localhost | awk 'NR>2' | grep 'open'", shell=True, universal_newlines=True)
    f = open('buffer.txt', 'w')
    f.write(port_open)
    f.close()
    f = open('buffer.txt', 'r')
    port_open = f.read()
    f = open('buffer.txt', 'w')
    f.write(port_open)
    f.close()
    f = open('buffer.txt', 'r')
    port_open = f.readlines()
    list = []
    for i in port_open:
        list.append(i[:-1])
    list_port = []
    list_service = []
    for i in list:
        index_open = i.find('open')
        list_port.append(((i[:index_open]).replace(" ", ""))[:-4])
        list_service.append((i[index_open+4:]).replace(" ", ""))
    flag_check = True
    for i in range(int(start_port), int(end_port) + 1):
        if (str(i) in list_port):
            if (flag_check):
                print('<h1>Открытые порты в введённом диапазоне: [{}:{}]</h1>\n'.format(start_port,end_port))
                flag_check = False
            element = list_port.index(str(i))
            print('<h2>Порт: {} | Сервис: {}</h2>\n'.format(i, list_service[element]))
    if (flag_check):
        print('<h1>В введённом диапазоне: [{}:{}] нет открытых портов</h1>'.format(start_port, end_port))
else:
    message = ""
    if (flag_start == False):
        message += "<h1>Не указан начальный порт</h1>\n"
    if (flag_end == False):
        message += "<h1>Не указан конечный порт</h1>\n"
    print('<h2>{}</h2>'.format(message))
