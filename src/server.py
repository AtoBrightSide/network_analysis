from http.server import BaseHTTPRequestHandler, HTTPServer


class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/users':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()

            initializer = SlackDatabaseInitializer()
            initializer.initialize_database()

            client = MongoClient('mongodb://localhost:27017/')
            db = client['slack_database']

        else:
            self.send_response(404)
            self.end_headers()


if __name__ == '__main__':

    server_address = ('localhost', 8080)
    httpd = HTTPServer(server_address, RequestHandler)

    print('Starting server...')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        httpd.server_close()
        print('Server stopped.')
