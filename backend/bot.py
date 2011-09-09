#!/usr/bin/python
"""
Super bot created at the Betaworks hackathon. Original author: Tom Germouahauhguh (some kinda euro-name, whatever).

Dependencies:
  easy_install dnspython
  easy_install xmpppy
"""

import sys
import xmpp
import re
import logging
import mongo

db = mongo.get_db('chatstats')


def handleMessage(conn, message):
    body = message.getBody()
    m = re.search('\[(.+?)\] (.*)|_(.+?) (.*)_', body)
    if not m:
        logging.warning("failed to get message from body: %s" % body)
        return

    user = m.group(1) or m.group(3)
    text = m.group(2) or m.group(4)

    print 'user %s said: %s' % (user, text)

    # Make sure the speaker is listed in the about collection.
    about_coll = db.about
    speakers = about_coll.find_one({'_id': 'speakers'}) or {'_id': 'speakers'}
    l = speakers.get('list', [])
    if user not in l:
        speakers['list'] = l + [user]
        about_coll.save(speakers)

    # Update message count.
    counts_coll = db.counts
    if not counts_coll.find_one({'_id': user}):
        counts_coll.save({'_id': user, 'counts': 0})
    counts_coll.update({'_id': user}, {'$inc': {'counts': 1}})


############################# bot logic stop #####################################

def StepOn(conn):
    try:
        conn.Process(1)
    except KeyboardInterrupt:
        return 0

    return 1

def GoOn(conn):
    while StepOn(conn):
        pass

def main():
    if len(sys.argv) < 3:
        print "Usage: bot.py username@server.net password"
        return 1

    jid = xmpp.JID(sys.argv[1])
    user, server, password = jid.getNode(), jid.getDomain(), sys.argv[2]

    conn = xmpp.Client(server)#debug=[])
    conres = conn.connect()
    if not conres:
        logging.error("Unable to connect to server %s!" % server)
        return 1

    if conres <> 'tls':
        logging.warning("unable to estabilish secure connection - TLS failed!")

    authres = conn.auth(user,password)
    if not authres:
        logging.error("Unable to authorize on %s - check login/password." % server)
        return 1

    if authres <> 'sasl':
        logging.warning("unable to perform SASL auth os %s. Old authentication method used!" % server)

    conn.RegisterHandler('message', handleMessage)
    conn.sendInitPresence()

    logging.info("Bot started.")
    GoOn(conn)

if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    sys.exit(main())
