#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage() # парсим форму 
if not "user" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>Пользователь не указан</title>\n") # заголовок страницы
        print("<h1>Пользователь не указан.</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
    user = form.getvalue("user") # получаем значение в переменную user
    print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
    print("<title>Пользователь: {}</title>\n".format(user)) # заголовок страницы
    count_proccess = subprocess.check_output("ps -u {} | wc -l".format(user), shell=True, stderr=subprocess.STDOUT, universal_newlines=True) # выполняем команду для получения процессов пользователя, потом их количество
    if (count_proccess.find("user name does not exist") != -1): # если найдена фраза user name does not exist
          print("<h1>Пользователь [{}] не найден в системе.</h1>".format(user)) # на странице будет написано, что пользователь не найден
    else: # иначе
        print("<h1>Количество процессов запущенных пользователем [{}]:\n{}</h1>\n".format(user,count_proccess)) # будет написана фраза и количество процессов
    print('<form method="post" action="cgi_user_proc.py"><input type="hidden" name="user" value="{}"><input type="submit" value="переопределить"></form>\n<br>\n'.format(user)) # кнопка рефреша
    print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)