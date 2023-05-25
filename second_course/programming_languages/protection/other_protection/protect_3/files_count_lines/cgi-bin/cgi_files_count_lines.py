#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage() # парсим форму 
if not "file" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>Файл не указан</title>\n") # заголовок страницы
        print("<h1>Файл не указан.</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
    file = form.getvalue("file") # получаем значение в переменную user
    print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
    print("<title>Файл: {}</title>\n".format(file)) # заголовок страницы
    try:
        content = subprocess.check_output('cat {}'.format(file), shell=True, stderr=subprocess.STDOUT, universal_newlines=True) # выполняем команду для получения содержимого файла в домашней директории
    except:
        print('<h2>Файла {} не существует'.format(file))
        exit(1)
    buff = open('buffer.txt', 'w') # записываем содержимое файла в файл buffer.txt
    buff.write(content)
    buff.close()
    buff = open('buffer.txt', 'r') # считываем содержимое файла из файла buffer.txt
    content = buff.readlines()
    print("<h1>Содержимое указанного файла [{}]</h1>\n".format(file)) # будет написано название файла
    count = 0
    for i in content: # цикл по строчкам из файла buffer.txt
        print("<h4>{}</h4>".format(i))
        count += 1
    print('<h2>Количество строчек в файле: {}'.format(count))
    print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)