#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

# функция проверки валидности IP
def isValidIP(s):
    if s.count('.') != 3:
        return 0
    l = list(map(str, s.split('.')))
    for ele in l:
        if int(ele) < 0 or int(ele) > 255 or (ele[0]=='0' and len(ele)!=1):
            return 0
    return 1

form = cgi.FieldStorage() # парсим форму 
if not "IP" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>IP для маршрута не указан</title>\n") # заголовок страницы
        print("<h1>IP не указан.</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
    IP = form.getvalue("IP") # получаем значение в переменную IP
    print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
    if (isValidIP(IP)):
        print("<title>Маршрут до: {}</title>\n".format(IP)) # заголовок страницы
        route = subprocess.check_output('traceroute -q 1 {} | cut -d"(" -f2 | cut -d")" -f1'.format(IP), shell=True, stderr=subprocess.STDOUT, universal_newlines=True) # выполняем команду для получения списка IP-адресов в маршруте до введённого хоста
        buff = open('buffer.txt', 'w') # записываем IPшники в файл buffer.txt
        buff.write(route)
        buff.close()
        buff = open('buffer.txt', 'r') # считываем IPшники из файла buffer.txt
        files = buff.readlines()
        print("<h1>IP-адреса в маршруте до хоста с IP {}:</h1>\n".format(IP)) # будет написан IP вместо фигурных скобок
        count = 0
        count_open = 0
        for i in files: # цикл по строчкам из файла buffer.txt
            if (count != 0 and count != len(files) - 1):
                if (i.find(' *') == -1):
                    print("<h4>{} - {}</h4>\n".format(count_open + 1,i))
                    count_open += 1
            count += 1
    else:
         print('<h1>Введён неверный IP</h1>\n')
    print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)