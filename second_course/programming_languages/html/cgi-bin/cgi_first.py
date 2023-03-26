#! /usr/bin/env python3

import cgi

def main():
    form = cgi.FieldStorage()
    print("Content-type: text/html\n")
    print("<title>Reply Page</title>")
    if not "user" in form:
        print("<h1>Who are you?</h1>")
    else:
        print("<h1>Hello <i>{}</i>!</h1>".format(form.getvalue("user")))
    return 0

if __name__ == "__main__":
    main()
