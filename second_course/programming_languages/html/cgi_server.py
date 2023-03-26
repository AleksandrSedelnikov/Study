import os
import http.server

def main():
    server_address = ("", 8000)
    os.chdir("/home/aleksandrsedelnikov/testing_page/3laba")
    server = http.server.HTTPServer
    handler = http.server.CGIHTTPRequestHandler
    httpd = server(server_address, handler)
    httpd.serve_forever()

if __name__ == "__main__":
    main()