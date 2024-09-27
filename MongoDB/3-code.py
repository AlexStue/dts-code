from pymongo import MongoClient
from pprint import pprint

# client = MongoClient(
#     host="127.0.0.1",
#     port = 27017,
#     username = "datascientest",
#     password = "dst123"
#)

client = MongoClient('mongodb://datascientest:dst123@127.0.0.1:27017/admin')  # Adjust as needed


# Test the connection
pprint("hello")
db = client['mydatabase']
databases = client.list_database_names()
print(databases)

# db = client.admin
# server_status = db.command("serverStatus")
# pprint(server_status)

