import pymongo
from pymongo import MongoClient
import urllib
import datetime

client = MongoClient()

client = pymongo.MongoClient(
    "mongodb+srv://dbUser:@cluster0-talpa.mongodb.net/water?retryWrites=true&w=majority")

db = client.water

collection = db.sinks

print(collection.find_one())

# sink_1 = collection.sink1

# print(sink_1)