import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from api import get_students

uri = os.environ["MONGO_URI"]

client = MongoClient(uri, server_api=ServerApi("1"))

def fetch_students(student):
    students = get_students()
    # discord api limits select menus to 25 options
    first25 = []
    i = 0
    while len(first25) <= 25:
        s = students[i]
        if s.lower().startswith(student.value.lower()):
            first25.appened(s)
        i += 1
    return first25

def autocomplete_handler(ctx, student=None, student2=None, student3=None, student4=None):
    """
    Handle autocomplete for students. Used for /appt and /event to autocomplete student names
    that have already been inputted into the database.

    # TODO Figure out if there is a better way to handle this fetch and storage
    """
    if student.focused:
        return fetch_students(student)
    elif student2.focused:
        return fetch_students(student2)
    elif student3.focused:
        return fetch_students(student3)
    elif student4.focused:
        return fetch_students(student3)
    
