from http.server import HTTPServer, BaseHTTPRequestHandler

class LocalOnlyHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.client_address[0] == '127.0.0.1':
            # Nur Anfragen von localhost erlauben
            super().do_GET()
        else:
            self.send_response(403)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Forbidden: Only localhost allowed.')

    def do_POST(self):
        if self.client_address[0] == '127.0.0.1':
            # Nur Anfragen von localhost erlauben
            super().do_POST()
        else:
            self.send_response(403)
            self.send_header('Content-type', 'text/plain')
            self.end_headers()
            self.wfile.write(b'Forbidden: Only localhost allowed.')

# Server starten
address = ('', 8000)  # Leerer String für alle verfügbaren Interfaces
server = HTTPServer(address, LocalOnlyHTTPRequestHandler)
server.serve_forever()
