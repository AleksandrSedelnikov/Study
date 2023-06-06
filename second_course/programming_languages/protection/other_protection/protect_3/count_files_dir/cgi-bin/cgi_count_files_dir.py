#! /usr/bin/env python3
# -*- coding: utf-8 -*-


import cgi
import subprocess
import os

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
if not "dir_name" in form:
        print("<title>Директория не указана</title>\n")
        print("<h1>Вы не указали директорию</h1>")
else:
    dir = form.getvalue("dir_name")
    print("<title>Проверка директории {}</title>\n".format(dir))
    if (os.path.isdir('{}'.format(dir))):
        count_files = subprocess.check_output("find {} -maxdepth 1 | wc -l".format(dir), shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        if (count_files.find('find:') == -1):
            print("<h1>Количество файлов в директории [{}]:{}</h1>\n".format(dir,count_files))
        else:
             print("<h1>Директория {} пустая".format(dir))
    else:
         print('<h1>Директория не найдена.</h1>')
