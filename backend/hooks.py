#!/usr/bin/python

import cherrypy
import json
import os.path

def json_wrap(func):
    def _decorated(*args, **kwargs):
        body = func(*args, **kwargs)
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps(body)
    return _decorated

class Hooks(object):

    def index(self, chatroom, speaker):
        return """
<html> <head><title> Chat Stats Hooks </title></head>
<body>
<h1> Chat Stats Hooks </h1>
<p> Hooks for interracting with partychat. You probably want to go <a href='/'>here</a>. </p>
</body>
"""

    #
    # Expose Handlers
    #
    index.exposed = True


def start():
    conf = os.path.join(os.path.dirname(__file__), 'server.conf')
    cherrypy.quickstart(Hooks(), config=conf)

if __name__ == '__main__':
    start()
