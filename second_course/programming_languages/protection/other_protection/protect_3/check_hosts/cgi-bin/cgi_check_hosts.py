#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage() # парсим форму 
if not "hosts" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>Хосты не выбраны</title>\n") # заголовок страницы
        print("<h1>Хосты не выбраны.</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
        hosts = form.getvalue("hosts") # получаем значение в переменную dns_servers
        hosts_list = str(hosts).split(",")
        hosts_from = []
        hosts_bad = []
        for i in hosts_list:
                ping = subprocess.check_output('ping -c 1 {} | grep rtt | cut -d"=" -f2 | cut -d"/" -f1'.format(i), shell=True, universal_newlines=True,stderr=subprocess.STDOUT)
                if (ping.find('ping') == -1):
                        if (len(ping) != 0):
                                hosts_from.append([i,float(ping[1:])])
                        else:
                                hosts_bad.append([i,"хост не ответил на ping"])
                else:
                        hosts_bad.append([i,"неверный IP-хоста"])
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        sorted_list = sorted(hosts_from, key=lambda x: x[1])
        print("<title>Проверка хостов</title>\n")
        if (len(sorted_list) != 0):
                print("<h2>Проверенные и отсортированные по времени хосты:</h2>")
                for i in range(len(sorted_list)):
                        if (i == 0):
                                print("<h3>IP-порта: {} || Время до хоста: {} ms || Комментарий: <B>самый ближний хост</B></h3>\n".format(sorted_list[i][0],sorted_list[i][1]))
                        else:
                                print("<h3>IP-порта: {} || Время до хоста: {} ms</B></h3>\n".format(sorted_list[i][0],sorted_list[i][1]))
        if (len(hosts_bad) != 0):
                print("<h2>Хосты с ошибками:</h2>\n")
                for i in range(len(hosts_bad)):
                        print("<h3>IP-порта: {} || Ошибка: {}</h3>\n".format(hosts_bad[i][0],hosts_bad[i][1]))
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
