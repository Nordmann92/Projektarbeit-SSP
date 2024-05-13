def choose_winner(self):

    if self.choose_random_move == self.choose_move:
        print("Unentschieden")
    elif self.choose_random_move == "1" or "scissor" and self.choose_move == "2" or "rock":
        self.score + 1
        self.win + 1
        print("Du hast gewonnen!")
    elif self.choose_random_move == "2" or "rock" and self.choose_move == "3" or "paper":
        self.score + 1
        self.win + 1
        print("Du hast gewonnen!")
    elif self.choose_random_move == "3" or "paper" and self.choose_move == "2" or "rock":
        self.score - 1
        p1.lose += 1
        print("Du hast verloren!")
    if self.choose_random_move == "1" or "scissor" and self.choose_move == "3" or "paper":
        self.score - 1
        self.lose + 1
        print("Du hast verloren!")
    if self.choose_random_move == "2" or "rock" and self.choose_move == "1" or "scissor":
        self.score - 1
        self.lose + 1
        print("Du hast verloren!")
    if self.choose_random_move == "3" or "paper" and self.choose_move == "1" or "scissor":
        self.score + 1
        self.win + 1
        print("Du hast gewonnen!")




def func(p1, p2):
    if p1.move == p2.move:
        print("unentschieden")
    elif p1.move == "rock" and p2.move == "scissor":
        print("Du hast GEWONNEN!")
        p1.score = p1.score + 1
        p1.win += 1
        p2