import cherrypy
import json
import mongo


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
    cherrypy.quickstart(ChatStatsApi())


if __name__ == '__main__':
    start()
