import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from api import get_students

uri = os.environ["MONGO_URI"]

client = MongoClient(uri, server_api=ServerApi("1"))

students = ["Ben"]


# TODO Figure out a better way to handle this storage and fetch
def autocomplete_fetch():
    """Fetch MongoDB for autocomplete options related to student and fulltimer selection"""

    global students
    students = get_students()


def autocomplete_handler(ctx, student=None):
    """filtering of students based on fulltimer selected

    once a fulltimer is chosen, this function autocompletes the student field
    with only students who are associated with that fulltimer.
    Useful for sister / brothers mainly to filter out the excess students
    https://github.com/breqdev/flask-discord-interactions/blob/main/examples/autocomplete.py
    """
    if student.focused:
        return [c for c in students if c.lower().startswith(student.value.lower())]
