from pymongo.mongo_client import MongoClient

uriN = "mongodb+srv://Norman:t2wGUYrYIvyMu077@norman1.tnxqh8h.mongodb.net/?retryWrites=true&w=majority&appName=Norman1"

# Create a new client and connect to the server
client = MongoClient(uriN)

# 1
db = client["SSP"]

# 2
collection = db['played_games']

# 3
# collection.insert_one({"Name": "Max", "Alter": 20, "Studiengang": "Informatik"})


# 4
# collection.update_one({"Name": "Max"},{"$set":{"Alter": 21}})

# 5
# collection.insert_one({"Name": "Bob", "Alter": 24, "Studiengang": "Wirtschaft"})
# collection.insert_one({"Name": "Jon", "Alter": 19, "Studiengang": "Bauwesen"})
# collection.insert_one({"Name": "Anna", "Alter": 23, "Studiengang": "Jura"})

# 6

# suche = collection.find_one({"Name": "Elisa"}, {"_id": 0})
# print(suche)

# 7

alle = collection.find({"player_1": "Elisa"}, {"_id": 0})
for doc in alle:
    print(doc)
"""
# 8

# collection.delete_one({'Name': 'Max'})

document_to_insert = {"vorname": "thomas", "nachname":"stark","age":55}
collection.insert_one(document_to_insert)

print(client.list_database_names())

"""