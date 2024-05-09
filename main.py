# main File

class Character:
    def __init__(self, name, score, win, lose, move):
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

