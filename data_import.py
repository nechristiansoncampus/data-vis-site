import gspread
import pymongo

import os
import json

# cript for importing data from old stats google sheet into Mongo

gc = gspread.service_account_from_dict(json.loads(os.environ["GOOGLE_SERVICE_CREDS"]))

sh = gc.open("MIT Student Updates")

# print(sh.sheet1.get('B2'))

list_of_dicts = sh.worksheet("Appt").get_all_records()
print(list_of_dicts[2])

{'Timestamp': '1/13/2020',
 'Student': 'Shulammite Lim',
 'Date': '1/13/20',
 'Full-Timers': 'Lisa ',
 'Summary': 'Had lunch together'}