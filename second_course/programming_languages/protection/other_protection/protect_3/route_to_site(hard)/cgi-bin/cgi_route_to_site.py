#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi
import subprocess

def ipFrom_Site(site):
    if (site != "null"):
        ip_addr = []
        result = subprocess.check_output("traceroute -q 1 {} | cut -d'(' -f2 | cut -d')' -f1".format(site),stderr=subprocess.STDOUT, shell=True, universal_newlines=True)
        if (result.find("Name or service not known") == -1):
            buff_save = open('buffer.txt', 'w')
            buff_save.write(result)
            buff_save.close()
            buff_read = open('buffer.txt', 'r')
            lines = buff_read.readlines()
            for i in lines:
                if (i.find("*") == -1):
                    ip_addr.append(i[:-1])
        else:
            ip_addr.append("Не найден введённый хост: {}".format(site))
        print("<h2>Проверка сайта: {}:</h2>\n".format(site))
        if (len(ip_addr) == 1):
            print("<table class='tb'>\n<caption>Ошибка в проверке:</caption>\n<tr>\n<th>#</th>\n<th>IP</th>\n<th>Комментарий</th>\n</tr>".format(site))
            print('<tr>\n')
            print('<td>1</td>\n<td>null</td>\n<td>{}</td>\n'.format(ip_addr[0]))
            print('</tr>')
        else:
            print("<table class='tb'>\n<caption>Список IP-адресов до сайта\n</caption>\n<caption>Site: {} | IP: {}\n</caption>\n<tr>\n<th>#</th>\n<th>IP</th>\n<th>Комментарий</th>\n</tr>".format(site,ip_addr[0]))
            num = 0
            for i in range(1,len(ip_addr) -1):
                print('<tr>\n')
                print('<td>{}</td>\n<td>{}</td>\n<td>{}</td>\n'.format(num + 1,ip_addr[i], "IP номер {}".format(num+1)))
                print('</tr>')
                num += 1
        print('</table>')
    else:
        print('<h1>Вы не указали имя/ip сайта.</h1>')
    return 0

def main():
    form = cgi.FieldStorage()
    print("Content-type: text/html; charset=utf-8\n")
    print('<style>\nbody {\nmargin: 50px 0;\npadding: 0;\n}\nth {\npadding: 10px;\nborder: 1px solid #000;\nborder-radius: 5%;}\ntd {\nfont-size: 0.9em;\npadding: 5px 7px;\nborder: 1px solid #000;\nborder-radius: 5%;\ntext-align: center; }\n</style>')
    if not "site" in form:
        print("<title>Сайт не указан</title>\n")
        ipFrom_Site("null")
    else:
        site = form.getvalue("site")
        print("<title>Проверка сайта {}</title>\n".format(site))
        ipFrom_Site(site)
    return 0

if __name__ == "__main__":
    main()
