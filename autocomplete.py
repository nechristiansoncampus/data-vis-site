# from pymongo.mongo_client import MongoClient
# from pymongo.server_api import ServerApi

# uri = "mongodb+srv://benfindeisen:PWDHERE@cluster0.yo8tuvl.mongodb.net/?retryWrites=true&w=majority"

# client = MongoClient(uri, server_api=ServerApi('1'))

fulltimers = ["Ben", "David", "Adrian"]
students = {
    "Ben": ["Noah", "Matt", "Andrew"],
    "David": ["Garett", "Ethan", "Isaac"],
    "Adrian": ["Zachia", "Remi", "Brenda"],
}

def autocomplete_fetch():
    pass
    # try:
    #     client.admin.command('ping')
    #     print("Pinged your deployment. You successfully connected to MongoDB!")
    # except Exception as e:
    #     print(e)
    # fters = []
    # db = client.people
    # col = db.fulltimers
    # print ("\nReturn every document:")
    # for doc in col.find():
    #     fters.append(doc["name"])
    # global fulltimers
    # fulltimers = fters


def autocomplete_handler(ctx, fulltimer=None, student=None):
    if fulltimer.focused:
        return [c for c in fulltimers if c.lower().startswith(fulltimer.value.lower())]
    elif student.focused:
        if fulltimer.value in students:
            return students[fulltimer.value]
        else:
            return []