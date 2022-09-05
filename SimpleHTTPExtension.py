#! /bin/python3
import socketserver
import http.server

class MyHTTP(http.server.SimpleHTTPRequestHandler):
    def handle_one_request(self):
        print(self)
        print(self.client_address[0])
        return super().handle_one_request()
httpd = socketserver.TCPServer(("", 8000), MyHTTP)

print("Now serving HTTP server on port 8000")

while True:
    httpd.handle_request()
