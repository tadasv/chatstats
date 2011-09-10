import pymongo

connection = None

def get_connection():
    global connection
    if not connection:
        connection = pymongo.Connection('localhost', 27017)
    return connection


def get_db(chatroom):
    conn = get_connection()
    db = conn[chatroom]
#    db.speakers.ensure_index('count')
    return db


def get_collection(db, username):
    """
    @param db: mongo db returned by get_db
    """
    return db[username]
