from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.q1zeowl.mongodb.net/pytech"
client = MongoClient(mongodb+srv://admin:adming@cluster0.q1zeowl.mongodb.net/pytech)
db = client.pytech
print(db.list_collection_names())
