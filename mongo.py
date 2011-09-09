import pymongo

connection = pymongo.Connection('localhost', 27017)
db = connection.chatstats
