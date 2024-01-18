import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = os.environ["MONGO_URI"]

client = MongoClient(uri, server_api=ServerApi("1"))


def test_db_conn():
    """Test for a db connection to Mongo Atlas"""
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)


def save_appointment(data):
    """Saves the data dictionary into the db"""
    db = client["mit-stats"]
    col = db.appointments
    col.insert_one(data)


def get_fulltimers():
    """Fetch a list of all the possible fulltimers/trainees"""
    fters = []
    db = client["mit-stats"]
    col = db.fulltimers
    for doc in col.find():
        fters.append(doc["name"])
    return fters
