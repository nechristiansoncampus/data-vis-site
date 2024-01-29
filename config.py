import os

testDB = "stats-test"
productionDB = "mit-stats"

activeDB = testDB
if os.environ["DEPLOYMENT_ENV"] == "PROD":
    activeDB = productionDB
