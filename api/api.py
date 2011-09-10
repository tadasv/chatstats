#!/usr/bin/python

import cherrypy
import json
import pymongo
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
    def list_speakers(self, chatroom, **kwargs):
        db = mongo.get_db(chatroom)
        about = db.about

        doc = about.find_one({'_id' : 'speakers'})
        if not doc:
            return {'list_speakers' : []}
        else:
            return {'list_speakers' : doc['list']}


    @json_wrap
    def top_speakers(self, chatroom, **kwargs):
        db = mongo.get_db(chatroom)
        docs = db.speakers.find(limit=15).sort('count', pymongo.DESCENDING)

        result = []
        for d in docs:
            result.append({'speaker' : d['_id'], 'messages' : d['count'], 'words': d['words'], 'chars' : d['chars']})

        return {'top_speakers' : result}

    top_speakers.exposed = True
    list_speakers.exposed = True


def start():
    conf = os.path.join(os.path.dirname(__file__), 'server.conf')
    cherrypy.quickstart(ChatStatsApi(), config=conf)

if __name__ == '__main__':
    start()
