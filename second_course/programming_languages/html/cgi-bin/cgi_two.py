#!/usr/bin/env python3

import cgi

def main():
    form = cgi.FieldStorage()
    print("Content-type: text/html\n")
    if "name" in form:
        name = form["name"].value
        print("<h1>Привет, {}!</h1>".format(name))
    else:
        print("<h1>Введите ваше имя!</h1>")
    return 0

if __name__ == "__main__":
    main()