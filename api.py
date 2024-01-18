import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from config import activeDB

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
    db = client[activeDB]
    col = db.appointments
    col.insert_one(data)


def get_students():
    """Fetch a list of all the possible fulltimers/trainees"""
    students = []
    db = client[activeDB]
    col = db.students
    for doc in col.find():
        students.append(doc["name"])
    return students
