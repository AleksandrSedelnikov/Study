import os
import http.server

def main():
    server_address = ("", 8000)
    os.chdir("своя директория с файлами")
    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    httpd = server(server_address, handler)
    httpd.serve_forever()

if __name__ == "__main__":
    main()