import random


class Character:
    def __init__(self, name, score=0, lose=0, win=0, move=0):
        self.name = name
        self.score = score
        self.lose = lose
        self.win = win
        self.move = move





class Player(Character):
    def choose(self):
        moves = ["Schere", "Stein", "Papier"]
        print("\nWähle deinen Zug:")
        for index, move in enumerate(moves, start=1):  # zB 1. Schere, 2. Stein, 3. Papier
            print(f"{index}. {move}")

        move = input("Gib die Nummer deines Zugs ein:")
        self.move = moves[int(move) - 1]


class Computer(Character):
    def choose(self):
        moves = ["Schere", "Stein", "Papier"]
        self.move = random.choice(moves)

p1 = Player("John")
print(p1.move)
p1.choose()
print(p1.move)

p2 = Computer("NPC")
p2.choose()
print(p2.move)