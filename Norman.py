def choose_winner(player_a, player_b) -> object:

    if player_a.move == player_b.move:
        return "Unentschieden"
    if ((player_a.move == "rock" and player_b.move == "scissor") or
            (player_a.move == "paper" and player_b.move == "rock") or
            (player_a.move == "scissor" and player_b.move == "paper")):
        player_a.score += 1
        player_a.win += 1
        player_b.score -= 1
        player_b.lose += 1
        return player_a.name
    if ((player_a.move == "rock" and player_b.move == "paper") or
            (player_a.move == "paper" and player_b.move == "scissor") or
            (player_a.move == "scissor" and player_b.move == "rock")):
        player_a.score -= 1
        player_a.lose += 1
        player_b.score += 1
        player_b.win += 1
        return player_b.name
    else:
        return "fehler"

