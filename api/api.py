#!/usr/bin/python

import cherrypy
import json
import mongo
import os.path

def json_wrap(func):
    def _decorated(*args, **kwargs):
        body = func(*args, **kwargs)

        jsonp = kwargs.get('jsonp', None)
        if jsonp:
            cherrypy.response.headers['Content-Type'] = 'text/javascript'
            return '%s(%s)' % (jsonp, json.dumps(body))
        else:
            cherrypy.response.headers['Content-Type'] = 'application/json'
            return json.dumps(body)
    return _decorated

class ChatStatsApi(object):

    @json_wrap
    def top_speakers(self, chatroom, **kwargs):
        db = mongo.get_db(chatroom)
	about = db.about

        result = [
            {'speaker' : 'tadas', 'lines' : 10, 'words' : 123, 'frequency' : 15.6},
            {'speaker' : 'heewa', 'lines' : 160, 'words' : 123, 'frequency' : 151.6},
            {'speaker' : 'aytan', 'lines' : 210, 'words' : 1293, 'frequency' : 10.6},
            {'speaker' : 'allan', 'lines' : 510, 'words' : 1253, 'frequency' : 15.6},
            {'speaker' : 'mona', 'lines' : 10, 'words' : 1323, 'frequency' : 5.6},
            {'speaker' : 'tony', 'lines' : 120, 'words' : 13423, 'frequency' : 15.6},
        ]
	return {'top_speakers' : result}

    top_speakers.exposed = True


def start():
    conf = os.path.join(os.path.dirname(__file__), 'server.conf')
    cherrypy.quickstart(ChatStatsApi(), config=conf)

if __name__ == '__main__':
    start()
