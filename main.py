# main File

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

def welcome():
    print('Willkommen zu unserem Spiel "Schere, Stein, Papier"')

def player_chose_name():
    a = input("Bitte gib deinen Spielernamen an: ")
    return a



def player_chose_move():
    a = input("Bitte wähle deinen Spielzug! Schere (1), Stein (2) oder Papier (3): ")
    a = a.lower()
    if a == "1" or a == "schere":
        return "scissor"
    elif a == "2" or a == "stein":
        return "rock"
    elif a == "3" or a == "papier":
        return "paper"
    else:
        print("Deine Eingabe war falsch!")
        return player_chose_move()


if __name__ == '__main__':
    print(player_chose_move())