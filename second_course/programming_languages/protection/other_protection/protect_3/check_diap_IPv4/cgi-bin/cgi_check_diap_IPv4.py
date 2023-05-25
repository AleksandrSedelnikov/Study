#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import ipaddress
import subprocess

# функция проверки правильности IP/mask
def isValidIP(s):
    if s.count('.') != 3:
        return 0
    l = list(map(str, s.split('.')))
    for ele in l:
        if int(ele) < 0 or int(ele) > 255 or (ele[0]=='0' and len(ele)!=1):
            return 0
    return 1

form = cgi.FieldStorage() # парсим форму 
if not "IP" in form or not "mask" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>IP или mask не указаны</title>\n") # заголовок страницы
        print("<h1>IP или mask не указаны</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
    IP = form.getvalue("IP") # получаем значение в переменную IP
    mask = form.getvalue("mask") # получаем значение в переменную mask
    print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
    print("<title>IP: {} | Mask: {}</title>\n".format(IP,mask)) # заголовок страницы
    if (isValidIP(IP) == 1 and isValidIP(mask) == 1):
        IP_list = []
        count = 0
        for x in ipaddress.ip_interface('{}/{}'.format(IP,mask)).network:
            IP_list.append(x)
            try:
                ping = subprocess.check_output('ping -c 1 {}'.format(x),shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
                print('<h2>Хост: {} доступен</h2>\n'.format(x))
                count += 1
            except:
                pass
        if (count == 0):
            print('<h2>Нет доступных хостов</h2>\n')
        else:
            print('<h2>Всего доступных хостов: {}</h2>'.format(count))
        print('<h2>Проверялось в диапазоне от {} до {}'.format(IP_list[0],IP_list[-1]))
    else:
        print('<h2>IP или маска указаны неверно</h2>\n')
    print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)