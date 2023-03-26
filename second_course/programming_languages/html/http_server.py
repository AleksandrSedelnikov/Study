import http.server 
import socketserver
server_address = ("", 8000)
handler_ = http.server.SimpleHTTPRequestHandler 
httpd = socketserver.TCPServer(server_address, handler_) 
httpd.serve_forever()