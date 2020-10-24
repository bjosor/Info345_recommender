import http.server
import socketserver

class Handler(http.server.SimpleHTTPRequestHandler):
    def do_HEAD(self):
        self.send_response(200)
        self.send_header('Content.type', 'text/html')
        self.end_headers()

    def do_GET(self):
        print('path is: ', self.path)
        if '/request' in self.path:
            respond('Good Stuff')
        else:
            super(Handler, self).do_GET()

    def handle_http(self, data):
        self.send_response(200)
        self.send_header('Content.type', 'application/json')
        self.end_headers()
        return bytes(data, 'UTF-8')

    def respond(self, data):
        response = self.handle_http(data)
        self.wfile.write(response)


if __name__ == '__main__':
    PORT = 8080

    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print("serving at port", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            httpd.server_close()
            print('Goodbye!')

'''
if __name__ == '__main__':
    server_address = ('', 8080)
    httpd = http.server.HTTPServer(server_address, Handler)
    print('server should be running')
    httpd.serve_forever()
'''
