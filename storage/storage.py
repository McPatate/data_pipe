from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.imgs

print('I forfeit, good night')
