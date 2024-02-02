import os
import json

database = "store_expenses.json"

def read_data():
    if not os.path.exists(database):
        return {}
    with json.open(database, 'r') as file:
        return json.load(file)