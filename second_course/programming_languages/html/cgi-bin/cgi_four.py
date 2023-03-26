#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

def proccess_info(flag,flags):
    try:
        if (flags[0][0] == 0 and flags[1][0] == 0):
            proccess = subprocess.check_output("ps -u",stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
        if (flags[0][0] == 1 and flags[1][0] == 0):
            proccess = subprocess.check_output("ps -u {}".format(flags[0][1]),stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
        if (flags[0][0] == 1 and flags[1][0] == 1):
            if (flags[1][1] == "mem"):
                proccess = subprocess.check_output("ps -u {} --sort=-rss".format(flags[0][1]),stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
            else:
                proccess = subprocess.check_output("ps -u {} --sort=-pcpu".format(flags[0][1]),stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
        if (flags[0][0] == 0 and flags[1][0] == 1):
            if (flags[1][1] == "mem"):
                proccess = subprocess.check_output("ps -u --sort=-rss",stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
            else:
                proccess = subprocess.check_output("ps -u --sort=-pcpu",stderr=subprocess.STDOUT,shell=True, universal_newlines=True)
        print(flag + "<h2>Полученная информация:</h2>\n")
        f = open('buff_proccess.txt', 'w')
        f.write(proccess)
        f.close()
        f = open('buff_proccess.txt', 'r')
        lines = f.readlines()
        for i in lines:
            print('<h4>{}</h4>'.format(i))
    except Exception as e:
        print(flag + "<h2>Полученная информация:</h2>\n")
        print('<h3>Введённого пользователя не существует.</h3>')
        print("Error: {}".format(e))
flag = "<h1>Общая статистика:</h1>\n<h2>Введённые данные:</h2>\n"
flags = [[0,0],[0,0]]
form = cgi.FieldStorage() # парсинг данных формы
print("Content-type: text/html; charset=utf-8\n") # http-заголовок плюс пустая строка
print("<title>Reply Page</title>\n") # html-разметка ответа
if not "user_name" in form:
    flag += '<h3>О своих процессах</h3>\n'
    flags[0][0] = 0
else:
    flags[0][0] = 1
    flags[0][1] = form.getvalue("user_name")
    flag += '<h3>О процессах: {}</h3>\n'.format(flags[0][1])
if not "typeproc" in form:
    flag += '<h3>Без сортировки</h3>\n'
    flags[1][0] = 0
else:
    flags[1][0] = 1
    flags[1][1] = form.getvalue("typeproc")
    flag += '<h3>С сортировкой: {}</h3>\n'.format(flags[1][1])
result = proccess_info(flags=flags,flag=flag)
