#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

form = cgi.FieldStorage()
print("Content-type: text/html; charset=utf-8\n")
users = subprocess.check_output("who | awk '{print $1}' | sort -u", shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
buff = open('buffer.txt','w')
buff.write(users)
buff.close()
buff = open('buffer.txt','r')
users = buff.readlines()
buff.close()
count = 0
for i in users:
        proccess = subprocess.check_output("ps -u {}".format(i[:-1]), shell=True, stderr=subprocess.STDOUT, universal_newlines=True)
        buff = open('buffer.txt','w')
        buff.write(proccess)
        buff.close()
        buff = open('buffer.txt','r')
        proc = buff.readlines()
        buff.close()
        print('<details>\n<summary>{}</summary>\n'.format(i[:-1]))
        for j in proc:
           print('<summary>{}</summary>\n'.format(j[:-1]))
        print('</details>\n')
        print('<h2>= = =</h2>')
        count += 1
print("<h3>Общее количество: {}</h3>\n".format(count))
print('<form method="post" action="cgi_users_online_proc.py"><input type="submit" value="переопределить"></form>\n<br>\n')