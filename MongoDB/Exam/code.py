import json
import os
from pymongo import MongoClient
from pprint import pprint

# Load data from the JSON file and insert it into MongoDB
from bson.objectid import ObjectId

# 
# def load_data_to_mongo():
#     json_file_path = os.path.expanduser('~/sample_training/books.json')
#     with open(json_file_path) as file:
#         for line in file:
#             book_data = json.loads(line)

#             # Convert the _id to ObjectId if necessary
#             if isinstance(book_data["_id"], dict) and "$oid" in book_data["_id"]:
#                 book_data["_id"] = ObjectId(book_data["_id"]["$oid"])

#             # Upsert each book record based on its unique identifier
#             db.books.update_one(
#                 {"_id": book_data["_id"]},
#                 {"$set": book_data},
#                 upsert=True
#             )

# (a) To connect to MongoDB via pymongo
client = MongoClient(
    host="localhost", # 127.0.0.1
    port=27017,
    username="datascientest",  # auth line 1
    password="dst123"    # auth line 2
)
print("Connected to MongoDBServer and Data Loaded")

# Write to Results
results = []

# Access database
db = client.sample

# Load data to MongoDB (do tell)
#load_data_to_mongo()

####################################################################################


# _Connexion à la base de données_ #

# (b) Display the list of available databases
db_list = client.list_database_names()
results.append(f"Display the available DBS: , {db_list}")

# (c) Display the list of collections available in this database
collection_list = db.list_collection_names()
results.append(f"Display Collections: , {collection_list}")

# (d) Display one of the documents in this collection
sample_document = db.books.find_one()
results.append(f"Display one document from books collection: , {sample_document}")

# (e) Display the number of documents in this collection
document_count = db.books.count_documents({})
results.append(f"Count number of documents in collection: , {document_count}")


# _Exploring the database_ #

# (a) Display the number of books with more than 400 pages
more_than_400_pages = db.books.count_documents({"pageCount": {"$gt": 400}})
more_than_400_pages_and_published = db.books.count_documents({"pageCount": {"$gt": 400}, "status": "PUBLISH"})
results.append(f"books with more_than_400_pages: , {more_than_400_pages}") 
results.append(f"books with more_than_400_pages_and_published: , {more_than_400_pages_and_published}")

# (b) Display the number of books with the keyword Android in their description
android_books_count = db.books.count_documents({
    "$or": [
        {"shortDescription": {"$regex": "Android", "$options": "i"}},
        {"longDescription": {"$regex": "Android", "$options": "i"}}
    ]
})
results.append(f"Number of books with Android in description: , {android_books_count}")

# (c) Display the 2 distinct category lists
distinct_categories = db.books.aggregate([
    {
        "$group": {
            "_id": None,
            "category1": {"$addToSet": {"$arrayElemAt": ["$categories", 0]}},
            "category2": {"$addToSet": {"$arrayElemAt": ["$categories", 1]}}
        }
    }
])
results.append(f"Distinct Categories: , {list(distinct_categories)}")

# (d) Display the number of books containing
languages_count = db.books.count_documents({
    "longDescription": {
        "$regex": "Python|Java|C\\+\\+|Scala",
        "$options": "i"
    }
})
results.append(f"Count on books containing programming languages: , {languages_count}")

# (e) Display various statistical information about our database
page_statistics = db.books.aggregate([
    {"$unwind": "$categories"},
    {
        "$group": {
            "_id": "$categories",
            "maxPages": {"$max": "$pageCount"},
            "minPages": {"$min": "$pageCount"},
            "averagePages": {"$avg": "$pageCount"}
        }
    }
])
results.append(f"Statistical info about pages per category: , {list(page_statistics)}")

# (f) Using a agregation pipeline
extracted_dates = db.books.aggregate([
    {"$match": {"publishedDate": {"$gte": "2009-01-01"}}},
    {
        "$project": {
            "title": 1,
            "year": {"$year": "$publishedDate"},
            "month": {"$month": "$publishedDate"},
            "day": {"$dayOfMonth": "$publishedDate"}
        }
    },
    {"$limit": 20}
])
results.append(f"Date for books published after 2009: , {list(extracted_dates)}")

# (g) From the list of authors, create new attributes
authors_attributes = db.books.aggregate([
    {
        "$project": {
            "title": 1,
            "author_1": {"$arrayElemAt": ["$authors", 0]},
            "author_2": {"$arrayElemAt": ["$authors", 1]},
            "author_3": {"$arrayElemAt": ["$authors", 2]},
        }
    },
    {"$limit": 20}
])
results.append(f"Updated Attributes: , {list(authors_attributes)}")

# (h) Based on the previous query, create a column containing
top_authors = db.books.aggregate([
    {
        "$group": {
            "_id": {"$arrayElemAt": ["$authors", 0]},
            "count": {"$sum": 1}
        }
    },
    {"$sort": {"count": -1}},
    {"$limit": 10}
])
results.append(f"Count of articles for first authors: , {list(top_authors)}")

####################################################################################

with open('res.txt', 'w') as file:
    for result in results:
        file.write(result + '\n')
        
pprint(results)
