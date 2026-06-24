from pymongo import MongoClient

uri = "mongodb+srv://odalys:odalys@cluster0.2cf9puv.mongodb.net/?appName=Cluster0"

client = MongoClient(uri)

db = client["Soccer_db"]

collection = db["teams"]
