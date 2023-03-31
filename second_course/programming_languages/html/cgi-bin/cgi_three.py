#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi

def main():
    flag = 0
    form = cgi.FieldStorage() # парсинг данных формы
    print("Content-type: text/html; charset=utf-8\n") # http-заголовок плюс пустая строка
    print("<title>Reply Page</title>") # html-разметка ответа
    generate = "<h1>Техническая статистика:</h1>\n"
    if not "name" in form: # проверка переданного атрибута ―user
        generate += "<h3>Не указано Имя</h3>\n"
        flag += 1
    if not "comment" in form:
        generate += "<h3>Не указан комментарий</h3>"
        flag += 1
    if not "browser" in form:
        generate += "<h3>Не указан тип браузера</h3>"
        flag += 1
    if flag == 0:
        name = form.getvalue("name")
        browser = form.getvalue("browser")
        if (browser == "ie"):
            browser = "Internet Explorer [code: {}]".format(browser)
        if (browser == "opera"):
            browser = "Opera [code: {}]".format(browser)
        if (browser == "ffox"):
            browser == "Firefox [code: {}]".format(browser)
        comment = form.getvalue("comment")
        generate = "<h1>Привет, милорд {}</h1>\n<h2>Выбранный браузер: {}</h2>\n<h3>Ваш комментарий: {}</h3>".format(name,browser,comment)
        print(generate)
    else:
        print(generate)
    return 0

if __name__ == "__main__":
    main()
