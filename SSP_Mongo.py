from pymongo.mongo_client import MongoClient
import datetime
from SSP_Mongo import *
from SSP_Core import *

uriN = "mongodb+srv://Norman:t2wGUYrYIvyMu077@norman1.tnxqh8h.mongodb.net/?retryWrites=true&w=majority&appName=Norman1"

client = MongoClient(uriN)
db = client["SSP"]
col_users = db['Users']
col_played_games = db["played_games"]

def check_user_name(player_1):
    searched_user = col_users.find_one({"name": player_1.name}, {"_id": 0})

    if searched_user == None:
        col_users.insert_one(player_1.__dict__)
    else:
        player_1.score = searched_user["score"]
        player_1.win = searched_user["win"]
        player_1.lose = searched_user["lose"]


def write_moves_to_collection(player_1, player_2, winner):
    now = datetime.datetime.now()
    col_played_games.insert_one({"time": now, "player_1": player_1.name, "player_1_move": player_1.move,
                                 "player_2": player_2.name, "player_2_move": player_2.move, "Winner": winner})


if __name__ == "__main__":
    try:
        client.admin.command('ping')
        print("Pinged your deployment. You successfully connected to MongoDB!")
    except Exception as e:
        print(e)
    p1 = Character("Norman")
    check_user_name(p1)
    print(p1.__dict__)