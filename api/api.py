import cherrypy
import json


def json_wrap(func):
    def _decorated(*args, **kwargs):
        body = func(*args, **kwargs)
        cherrypy.response.headers['Content-Type'] = 'application/json'
        return json.dumps(body)
    return _decorated

class ChatStatsApi(object):

    @json_wrap
    def top_speakers(self, chatroom, speaker):
        return {'username' : 1231123, 'test' : 'asdfasdf'}
    top_speakers.exposed = True


def start():
    cherrypy.quickstart(ChatStatsApi())


if __name__ == '__main__':
    start()
