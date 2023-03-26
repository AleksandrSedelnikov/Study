#!/usr/bin/env python3

import cgi

# получаем данные формы
form = cgi.FieldStorage()

# устанавливаем тип содержимого веб-страницы
print("Content-type: text/html\n")

# получаем значение поля "name" и выводим сообщение
if "name" in form:
    name = form["name"].value
    print("<h1>Привет, {}!</h1>".format(name))
else:
    print("<h1>Введите ваше имя!</h1>")