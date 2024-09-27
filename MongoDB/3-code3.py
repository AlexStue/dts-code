from pymongo import MongoClient
from pymongo.errors import ConnectionFailure

client1 = MongoClient('127.0.0.1', 27017, serverSelectionTimeoutMS=5000)
print(client1.admin.command('ping'))
print("MongoDB without user is running.")

client2 = MongoClient(
    host="127.0.0.1",
    port = 27017,
    username = "datascientest",
    password = "dst123"
)
print(client2.admin.command('ping'))
print("MongoDB user is running.")

databases = client2.list_database_names()
print("Databases:", databases)




