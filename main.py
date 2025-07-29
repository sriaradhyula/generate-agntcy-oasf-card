import http.server
import socketserver
import webbrowser
from pathlib import Path

# Serve the external index.html file
INDEX_FILE = Path(__file__).parent / "index.html"

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/' or self.path == '/index.html':
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            with open(INDEX_FILE, 'rb') as f:
                self.wfile.write(f.read())
        else:
            self.send_error(404, "File not found")

if __name__ == "__main__":
    PORT = 10000
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving UI at http://localhost:{PORT}")
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()
