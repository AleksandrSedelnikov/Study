#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess


form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")

if not "a" in form:
    print("<h2>Вы не указали права для поиска</h2>\n")
    print("<title>Права не указаны</title>\n") # заголовок страницы
    print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else:
    permission = [['-','-','-'],['-','-','-'],['-','-','-']]
    permissions = form.getvalue("a")
    for i in permissions:
        # пользователь
        if (i == "u_read"):
            permission[0][0] = 'r'
        if (i == "u_write"):
            permission[0][1] = 'w'
        if (i == "u_exec"):
            permission[0][2] = 'x'
        # группа
        if (i == "g_read"):
            permission[1][0] = 'r'
        if (i == "g_write"):
            permission[1][1] = 'w'
        if (i == "g_exec"):
            permission[1][2] = 'x'
        # остальные
        if (i == "o_read"):
            permission[2][0] = 'r'
        if (i == "o_write"):
            permission[2][1] = 'w'
        if (i == "o_exec"):
            permission[2][2] = 'x'
    pravo = ''.join(permission[0]) + ''.join(permission[1]) + ''.join(permission[2])
    print("<title>Поиск по правам: {}</title>\n".format(pravo))
    cur_stroka = "find ~ "
    for i in range(len(permission)):
        for j in permission[i]:
            if (i == 0):
                if (j != '-'):
                    cur_stroka += '-perm /u={} '.format(j)
            if (i == 1):
                if (j != '-'):
                    cur_stroka += '-perm /g={} '.format(j)
            if (i == 2):
                if (j != '-'):
                    cur_stroka += '-perm /o={} '.format(j)
    cur_stroka += '-type f'
    print('<h2>Информация по поиску файлов с правами: {}</h2>'.format(pravo))
    files = subprocess.check_output(cur_stroka,shell=True, universal_newlines=True)
    buff = open('buffer.txt','w')
    buff.write(files)
    buff.close()
    buff = open('buffer.txt', 'r')
    lines = buff.readlines()
    buff.close()
    print("<h2>Найденные файлы:</h2>")
    if (len(lines) == 0):
        print('<h3>Файлы не найдены</h3>')
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
    else:
        for i in lines:
            print('<h3>{}</h3>\n'.format(i))
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
    