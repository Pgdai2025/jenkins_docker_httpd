from http.server import SimpleHTTPRequestHandler, HTTPServer

class CustomHandler(SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        print(f"[REQUEST] {self.address_string()} - {self.log_date_time_string()} - {format % args}")

HOST = "0.0.0.0"
PORT = 8080

def run_server():
    with HTTPServer((HOST, PORT), CustomHandler) as httpd:
        print(f"✅ Server running at http://{HOST}:{PORT}")
        httpd.serve_forever()

if __name__ == "__main__":
    run_server()

