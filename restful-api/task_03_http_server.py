#!/usr/bin/python3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

class a(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.handle_root()
        elif self.path == '/data':
            self.handle_data()
        elif self.path == '/status':
            self.handle_status()
        else:
            self.handle_404()

    def handle_root(self):
        """H"""
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Hello, this is a simple API!")

    def handle_data(self):
        """D"""
        response_data = {
                "name": "John",
                "age": 30,
                "city": "New York"
        }
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        self.wfile.write(json.dumps(response_data).encode('utf-8'))

    def handle_404(self):
        """Handels error"""
        self.send_response(404)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Endpoint not found")

def run(server_class=HTTPServer, handler_class=a, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print("Starting  server  on port {}...".format(port))
    httpd.serve_forever()

if __name__ == "__main__":
    run()
