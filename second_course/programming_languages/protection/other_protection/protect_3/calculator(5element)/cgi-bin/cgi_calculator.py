#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import cgi

form = cgi.FieldStorage() # парсим форму 
if not "one_chislo" in form or not "two_chislo" in form or not "variant" in form: # если ничего туда не написано
        print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
        print("<title>Неверные входные данные</title>\n") # заголовок страницы
        print("<h1>Числа или действие над ними не указаны</h1>") # текст на странице
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)
else: # если что-то есть
    one_chislo = form.getvalue("one_chislo") # получаем значение в переменную one_chislo
    two_chislo = form.getvalue("two_chislo") # получаем значение в переменную two_chislo
    var = form.getvalue("variant") # получаем значение в переменную var
    print("Content-type: text/html; charset=utf-8\n") # стандартный тип контента
    print("<title>1: {} | 2: {} | {}</title>\n".format(one_chislo,two_chislo,var)) # заголовок страницы
    try:
        one = float(one_chislo)
        two = float(two_chislo)
    except:
        print('<h2>Какое-то число введено неверно</h2>\n')
        print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n')
        exit(1)
    if (var == "*"):
        result = one * two
    elif (var == "/"):
        result = one / two
    elif (var == "^"):
        try:
            result = one ** two
        except:
            result = "слишком большие входные данные"
    elif (var == "+"):
        result = one + two
    elif (var == "-"):
        result = one - two
    print('<h2>Тип действия: [{}]</h2>\n'.format(var))
    print('<h2>Ответ: {}</h2>'.format(result))
    print('<form><input type="button" value="назад" onclick="window.history.back()"></form>\n') # кнопка обратно (по истории браузера)