
#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
if "sentences" not in form:
    check_flag = True
    sentences = ""
else:
    check_flag = False
    sentences = form.getvalue("sentences")
users = subprocess.check_output("who | awk '{print $1}' | sort -u", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
if (check_flag):
    print("<h1>Пользователи онлайн:</h1>\n")
else:
    print("<h1>Пользователи онлайн с фразой {}:</h1>\n".format(sentences))
buff = open('buffer.txt','w')
buff.write(users)
buff.close()
buff = open('buffer.txt','r')
users = buff.readlines()
buff.close()
count = 0
for i in users:
    if (check_flag):
        print("<h2>{}</h2>\n".format(i[:-1]))
        count += 1
    else:
        if (i.find(sentences) != -1):
            print("<h2>{}</h2>\n".format(i[:-1]))
            count += 1
print("<h3>Общее количество: {}</h3>\n".format(count))
print('<form method="post" action="cgi_users_online_sentences.py"><input type="hidden" name="sentences" value="{}"><input type="submit" value="переопределить"></form>\n<br>\n'.format(sentences))