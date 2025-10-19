#!/usr/bin/python3
"""
A simple API built using Python's http.server module.
Handles GET requests for multiple endpoints:
    /           → Returns a greeting message
    /data       → Returns a JSON dataset
    /status     → Returns "OK"
    /info       → Returns API info
Other paths    → Returns 404 Not Found
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleAPIHandler(BaseHTTPRequestHandler):
    """Custom request handler for our simple API."""

    def do_GET(self):
        """Handle GET requests."""
        # Define routes
        if self.path == '/':
            self._send_text_response(200, "Hello, this is a simple API!")

        elif self.path == '/data':
            data = {"name": "John", "age": 30, "city": "New York"}
            self._send_json_response(200, data)

        elif self.path == '/status':
            self._send_text_response(200, "OK")

        elif self.path == '/info':
            info = {"version": "1.0", "description": "A simple API built with http.server"}
            self._send_json_response(200, info)

        else:
            # Unknown endpoint
            self._send_text_response(404, "Endpoint not found")

    def _send_text_response(self, code, message):
        """Helper to send plain text responses."""
        self.send_response(code)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(message.encode("utf-8"))

    def _send_json_response(self, code, data):
        """Helper to send JSON responses."""
        self.send_response(code)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        json_str = json.dumps(data)
        self.wfile.write(json_str.encode("utf-8"))


def run(server_class=HTTPServer, handler_class=SimpleAPIHandler):
    """Run the HTTP server."""
    server_address = ('', 8000)
    httpd = server_class(server_address, handler_class)
    print("Starting server on port 8000...")
    print("Visit http://localhost:8000 to test.")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
