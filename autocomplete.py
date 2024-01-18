import os
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from api import get_fulltimers

uri = os.environ["MONGO_URI"]

client = MongoClient(uri, server_api=ServerApi("1"))

fulltimers = ["Ben", "David", "Adrian"]
students = {
    "Ben": ["Noah", "Matt", "Andrew"],
    "David": ["Garett", "Ethan", "Isaac"],
    "Adrian": ["Zachia", "Remi", "Brenda"],
}


def autocomplete_fetch():
    """Fetch MongoDB for autocomplete options related to student and fulltimer selection"""
    global fulltimers
    fulltimers = get_fulltimers()


def autocomplete_handler(ctx, fulltimer=None, student=None):
    """filtering of students based on fulltimer selected

    once a fulltimer is chosen, this function autocompletes the student field
    with only students who are associated with that fulltimer.
    Useful for sister / brothers mainly to filter out the excess students
    """
    if fulltimer.focused:
        return [c for c in fulltimers if c.lower().startswith(fulltimer.value.lower())]
    elif student.focused:
        if fulltimer.value in students:
            return students[fulltimer.value]
        else:
            return []
