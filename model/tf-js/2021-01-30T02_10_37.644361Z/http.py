import SimpleHTTPServer
import SocketServer
import urllib
import urllib2

# Variables
URL = 'localhost:8000'
PORT = 8000

# Setup simple sever
Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()

# Getting HTML from the target page
values = {
    'name': 'Thomas Anderson',
    'location': 'unknown'
}
data = urlilib.urlencode(values)
req = urllib2.Request(url, data)
response = urllib2.urlopen(req)
html = response.read()