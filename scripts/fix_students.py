import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import ReturnDocument
from bson.objectid import ObjectId


uri = os.environ["MONGO_URI"]

client = MongoClient(uri, server_api=ServerApi("1"))

def get_fulltimers():
    """Fetch a list of all the possible students"""
    db = client["mit-stats"]
    collection = db.appointments
    for doc in collection.find():
        update_fulltimer_field(doc, collection)

def update_fulltimer_field(doc, collection):
    fulltimer_arr = doc["fulltimers"].split(", ")
    doc_id = doc["_id"]
        # Define the filter criteria to identify the document to update
    filter_criteria = {"_id": doc_id}

    # Define the update operation
    update_operation = {"$set": {"fulltimers": fulltimer_arr}}

    # Update a single document
    update_result = collection.update_one(filter_criteria, update_operation)

    # Check if a document was modified
    if update_result.modified_count > 0:
        print("Document updated successfully.")
    else:
        print("No document matched the filter criteria.")

get_fulltimers()

