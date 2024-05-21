import random
# random.seed(1)
from pymongo.mongo_client import MongoClient
import datetime


uriN = "mongodb+srv://Norman:t2wGUYrYIvyMu077@norman1.tnxqh8h.mongodb.net/?retryWrites=true&w=majority&appName=Norman1"

client = MongoClient(uriN)
db = client["SSP"]
col_users = db['Users']
col_played_games = db["played_games"]

# region Klasse Character
class Character:
    def __init__(self, name, score=0, win=0, lose=0, move=0):

        self.name = name
        self.score = score
        self.win = win
        self.lose = lose
        self.move = move

    def show_score(self):
        return self.score

    def show_move(self):
        return self.move

    def show_attributes(self):
        print(self.name, self.score, self.win, self.lose, self.move)

    def choose_random_move(self):
        moves = ["rock", "paper", "scissor"]
        self.move = random.choice(moves)

    def choose_move(self):
        a = input("Bitte wähle deinen Spielzug! Schere (1), Stein (2) oder Papier (3): ")
        a = a.lower()
        if a == "1" or a == "schere":
            self.move = "scissor"
        elif a == "2" or a == "stein":
            self.move = "rock"
        elif a == "3" or a == "papier":
            self.move = "paper"
        else:
            print("Deine Eingabe war falsch!")
            return self.choose_move()

    def choose_name(self):
        player1 = input("Bitte gib deinen Namen ein: ").lower()
        self.name = player1.capitalize()


def choose_winner(player_a, player_b) -> object:

    if player_a.move == player_b.move:
        return "Unentschieden"
    elif ((player_a.move == "rock" and player_b.move == "scissor") or
            (player_a.move == "paper" and player_b.move == "rock") or
            (player_a.move == "scissor" and player_b.move == "paper")):
        player_a.score += 1
        player_a.win += 1
        player_b.score -= 1
        player_b.lose += 1
        return player_a.name
    elif ((player_a.move == "rock" and player_b.move == "paper") or
            (player_a.move == "paper" and player_b.move == "scissor") or
            (player_a.move == "scissor" and player_b.move == "rock")):
        player_a.score -= 1
        player_a.lose += 1
        player_b.score += 1
        player_b.win += 1
        return player_b.name
    else:
        return "fehler"

# endregion

if __name__ == "__main__":

    print('Willkommen zu unserem Spiel "Schere, Stein, Papier"\n')
    p1 = Character("")
    p2 = Character("NPC")
    p1.choose_name()
    print()

    searched_user = col_users.find_one({"name": p1.name}, {"_id": 0})

    if searched_user == None:
        col_users.insert_one(p1.__dict__)
    else:
        p1.score = searched_user["score"]
        p1.win = searched_user["win"]
        p1.lose = searched_user["lose"]
        print(f"der Spieler {p1.name} existiert bereits! folgende Spielstände werden übernommen:")
        print(f"Punktestand: {p1.score}\ngewonnene Spiele: {p1.win}\nverlorene Spiele: {p1.lose}")

    while True:
        p2.choose_random_move()
        p1.choose_move()
        print()
        print(f"folgende Spielzüge wurden gewählt:\n{p1.name} : {p1.move}\n{p2.name} : {p2.move}\n")

        winner = choose_winner(p1, p2)
        now = datetime.datetime.now()

        print(f"der Gewinner ist: {winner}\n")

        retry = input("nochmal? (ja / nein): ")

        # Spiele in played_games schreiben
        col_played_games.insert_one({"time": now, "player_1": p1.name, "player_1_move": p1.move, "player_2": p2.name,
                                     "player_2_move": p2.move, "Winner": winner})

        if retry == "ja":
            pass
        else:
            if searched_user == None:
                a = f"aktuelle Sitzung: Score: {p1.score}, Wins: {p1.win}, Loses: {p1.lose}"
            else:
                a = f"aktuelle Sitzung: Score: {p1.score - searched_user["score"]}, Wins: {p1.win - searched_user["win"]}, Loses: {p1.lose - searched_user["lose"]}"
            break

    col_users.update_one({"name": p1.name}, {"$set": {"score": p1.score, "win": p1.win, "lose": p1.lose}})

    print(f"Deine Ergebnisse {p1.name}:")
    print(a)
    print(f"Gesamt: Score: {p1.score}, Wins: {p1.win}, Loses: {p1.lose}")
