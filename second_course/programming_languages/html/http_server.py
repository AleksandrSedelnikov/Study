import http.server 
import socketserver

def main():
    server_address = ("", 8000)
    handler_ = http.server.SimpleHTTPRequestHandler 
    httpd = socketserver.TCPServer(server_address, handler_) 
    httpd.serve_forever()

if __name__ == "__main__":
    main()