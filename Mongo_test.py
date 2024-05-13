from pymongo.mongo_client import MongoClient

uriE = "mongodb+srv://Elisa:0Rp1lJCVsfxaweF4@norman1.tnxqh8h.mongodb.net/?retryWrites=true&w=majority&appName=Norman1"

uriM = "mongodb+srv://Marilena:akpnKlRoeEDtVp0o@norman1.tnxqh8h.mongodb.net/?retryWrites=true&w=majority&appName=Norman1"

uriN = "mongodb+srv://Norman:t2wGUYrYIvyMu077@norman1.tnxqh8h.mongodb.net/?retryWrites=true&w=majority&appName=Norman1"

# Create a new client and connect to the server
client = MongoClient(uriN)

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)
