#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage() # парсим форму 
if not "dns" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>DNS-сервера для поиска не выбраны</title>\n") # заголовок страницы
        print("<h1>DNS-сервера для поиска не выбраны.</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
        dns_servers = form.getvalue("dns") # получаем значение в переменную dns_servers
        dns_correct = []
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        if (type(dns_servers) is list):
                print("<title>Проверка {} DNS-серверов</title>\n".format(len(dns_servers))) # заголовок страницы
                print("<h1>Проверка {} DNS-серверов</h1>\n".format(len(dns_servers))) # текст на странице
                for i in dns_servers:
                        count_uzl = subprocess.check_output('traceroute -q 1 {} | wc -l'.format(i),shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                        dns_correct.append([i,int(count_uzl) -2])
        else:
                print("<title>Проверка DNS-сервера</title>\n") # заголовок страницы
                print("<h1>Проверка DNS-сервера</h1>\n") # текст на странице
                count_uzl = subprocess.check_output('traceroute -q 1 {} | wc -l'.format(dns_servers),shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                dns_correct.append([dns_servers,int(count_uzl) -2])
        sorted_list = sorted(dns_correct, key=lambda x: x[1])
        for i in range(len(sorted_list)):
                print("<h3>DNS-сервер: {} || Количество узлов при обращении к DNS: {}</h3>\n".format(sorted_list[i][0],sorted_list[i][1]))