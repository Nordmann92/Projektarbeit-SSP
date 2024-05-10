

class Character():
    def __init__(self, name, score=0, lose=0, win=0, move=0):
        self.name = name
        self.score = score
        self.lose = lose
        self.win = win
        self.move = move


    def show_score(self):
        return self.score

    def show_move(self):
        return self.move



def select_player():
    player1 = input("Bitte gib deinen Namen ein: ").lower()
    return player1.capitalize()


def player_move():
    p_move = input("Bitte wähle 1 für Stein 2 für Schere 3 für Papier:")
    if p_move == "1":
        return "rock"
    elif p_move == "2":
        return "scissor"
    elif p_move == "3":
        return "paper"
    else:
        print("ungültige Eingabe")
        return player_move()




"""    

print("Willkommen zu Stein, Schere, Papier!")
player = select_player()

print(player)
"""

print(player_move())





