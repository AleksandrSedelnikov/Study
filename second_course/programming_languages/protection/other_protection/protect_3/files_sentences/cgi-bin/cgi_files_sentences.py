#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage() # парсим форму 
if not "sentences" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>Фраза поиска не указана</title>\n") # заголовок страницы
        print("<h1>Фраза не указана.</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
    sentences = form.getvalue("sentences") # получаем значение в переменную user
    print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
    print("<title>Поиск по фразе: {}</title>\n".format(sentences)) # заголовок страницы
    files = subprocess.check_output('grep "{}" -Rl ~ 2>~/error | cut -d":" -f1 | sed "s|.*/||"'.format(sentences), shell=True, stderr=subprocess.STDOUT, universal_newlines=True) # выполняем команду для получения файлов в домашней директории, в которых есть фраза
    buff = open('buffer.txt', 'w') # записываем названия файлов в файл buffer.txt
    buff.write(files)
    buff.close()
    buff = open('buffer.txt', 'r') # считываем названия файлов из файла buffer.txt
    files = buff.readlines()
    print("<h1>Названия файлов, в которых встретилась фраза [{}]</h1>\n".format(sentences)) # будет написана фраза
    for i in files: # цикл по строчкам из файла buffer.txt
        print("<h4>{}</h4>".format(i))
    print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)