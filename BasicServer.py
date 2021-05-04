#from urllib.parse import urlparse
import urllib.parse
#from urllib.parse import urlparse
from http.server import BaseHTTPRequestHandler, HTTPServer, SimpleHTTPRequestHandler
import json
from ResponseHandler import doGetResponse

class GetHandler(SimpleHTTPRequestHandler):
        def do_GET(self):
            parameters = urllib.parse.parse_qs(
                urllib.parse.urlparse(self.path).query)
            response = json.dumps(doGetResponse(parameters))
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.send_header("Content-length", len(response))
            self.end_headers()
            self.wfile.write(bytes(response, encoding='utf8'))
            #SimpleHTTPRequestHandler.do_GET(self)

Handler = GetHandler

httpd = HTTPServer(("localhost", 8080), Handler)
httpd.serve_forever()
