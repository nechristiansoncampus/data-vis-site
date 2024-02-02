import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from pymongo import ReturnDocument
from bson.objectid import ObjectId

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
    """Saves the appointment data dictionary into the db"""
    db = client[activeDB]
    col = db.appointments
    col.insert_one(data)


def get_event(id_str):
    db = client[activeDB]
    col = db.attendance
    return col.find_one({'_id': ObjectId(id_str)})


def save_event(data):
    """Saves the event data dictionary into the db, returns ObjectID str of saved event"""
    db = client[activeDB]
    col = db.attendance
    event_id = col.insert_one(data).inserted_id
    return str(event_id)


def add_one_attendee_to_event(id_str, attendee):
    """Adds one attendee to a given event
    
    id_str - (str) hexadecimal str that can be converted to MongoDB ObjectId (https://www.mongodb.com/developer/products/mongodb/bson-data-types-objectid/)
    attendee - (str) full name of student attendee to be added to the event attendance document

    returns the updated event document in dictionary form
    """
    db = client[activeDB]
    col = db.attendance
    return col.find_one_and_update(
        {'_id': ObjectId(id_str)},
        {'$push': {'attendees': attendee}},
        return_document=ReturnDocument.AFTER)


def save_student(firstname, lastname, classOf=""):
    data = {"firstname": firstname, "lastname": lastname, "classOf": classOf}
    db = client[activeDB]
    col = db.students
    if col.find_one({"firstname": firstname, "lastname": lastname}):
        return
    col.insert_one(data)


def get_students():
    """Fetch a list of all the possible students"""
    students = []
    db = client[activeDB]
    col = db.students
    for doc in col.find():
        students.append(doc["firstname"] + " " + doc["lastname"])
    return students
