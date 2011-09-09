#!/usr/bin/python

import cherrypy
import json
import mongo
import os.path

def json_wrap(func):
    def _decorated(*args, **kwargs):
        body = func(*args, **kwargs)
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps(body)
    return _decorated

class ChatStatsApi(object):

    @json_wrap
    def top_speakers(self, chatroom):
        db = mongo.get_db(chatroom)

        result = [
            {'speaker' : 'tadas'}
        ]

    top_speakers.exposed = True


def start():
    conf = os.path.join(os.path.dirname(__file__), 'server.conf')
    cherrypy.quickstart(ChatStatsApi(), config=conf)

if __name__ == '__main__':
    start()
