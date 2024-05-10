# main File
import random
# random.seed(1)
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


if __name__ == "__main__":
    print('"Willkommen zu unserem Spiel "Schere, Stein, Papier"')
    p1 = Character("")
    p1.choose_name()
    p1.choose_move()
    p1.show_attributes()
    p2 = Character("NPC")
    p2.choose_random_move()
    p2.show_attributes()



