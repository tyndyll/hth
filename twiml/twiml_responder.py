#!/usr/bin/env python

import os, sys

from BaseHTTPServer import BaseHTTPRequestHandler

class GetHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()
        s.wfile.write('''Response>
    <Dial timeout="10" record="false">{}</Dial>
</Response>'''.format(os.environ['TWIML_PHONE'])

if __name__ == '__main__':
    if 'TWIML_PHONE' not in os.environ:
        print 'TWIML_PHONE not set'
        sys.exit()
    from BaseHTTPServer import HTTPServer
    server = HTTPServer(('localhost', 8080), GetHandler)
    print 'Starting server, use <Ctrl-C> to stop'
    server.serve_forever()
