#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage() # парсим форму 
if not "sentences" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>Фраза не указана</title>\n") # заголовок страницы
        print("<h1>Фраза не указана.</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
    sentences = form.getvalue("sentences") # получаем значение в переменную sentences
    print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
    print("<title>Фраза поиска: {}</title>\n".format(sentences)) # заголовок страницы
    try:
        files = subprocess.check_output('find ~ -name "*{}*" -type f | sed "s|.*/||"'.format(sentences), shell=True, stderr=subprocess.STDOUT, universal_newlines=True) # выполняем команду для получения списка файлов в имени которых есть фраза в домашней директории
    except:
        print('<h2>Файлов с фразой {} не существует'.format(sentences))
        exit(1)
    buff = open('buffer.txt', 'w') # записываем список файлов в файл buffer.txt
    buff.write(files)
    buff.close()
    buff = open('buffer.txt', 'r') # считываем список файлов из файла buffer.txt
    files = buff.readlines()
    print("<h1>Файлы с фразой в названии [{}]</h1>\n".format(sentences)) # будет написана фраза
    count = 0
    for i in files: # цикл по строчкам из файла buffer.txt
        print("<h4>{}</h4>".format(i))
        count += 1
    print('<h2>Количество файлов: {}'.format(count))
    print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)