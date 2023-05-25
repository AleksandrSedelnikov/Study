#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage() # парсим форму 
if not "ipaddr" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>IP не установлен</title>\n") # заголовок страницы
        print("<h1>Не введён IP.</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
        ip = form.getvalue("ipaddr") # получаем значение в переменную dns_servers
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>MAC-адрес для IP: {}</title>\n".format(ip)) # заголовок страницы
        mac = subprocess.check_output('arp -a {}'.format(ip), shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        if (mac.find('entries no match found') == -1):
                start = mac.find('at')
                end = mac.find('[')
                print('<h2>MAC-адрес для IP [{}]: {}'.format(ip,mac[start+3:end]))
        else:
                print('<h1>Указанный IP [{}] недоступен'.format(ip))
                