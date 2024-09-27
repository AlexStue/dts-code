from pymongo import MongoClient

# Correct connection string with username and password
client = MongoClient('mongodb://datascientest:dst123@localhost:27017/')

# Access a database (it will be created if it does not exist)
db = client['mydatabase']

# Access a collection (it will be created if it does not exist)
collection = db['mycollection']

# Insert a document
try:
    result = collection.insert_one({"name": "John", "age": 30})
    print("Inserted document ID:", result.inserted_id)

    # Retrieve a document
    document = collection.find_one({"name": "John"})
    print("Retrieved document:", document)

except Exception as e:
    print("An error occurred:", e)

finally:
    # Close the connection
    client.close()


#docker run --name my-mongo -d -p 27017:27017 -e MONGO_INITDB_ROOT_USERNAME=root -e MONGO_INITDB_ROOT_PASSWORD=password mongo
