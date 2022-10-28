def who_won(game_board: list):
    p1_pieces = 0
    p2_pieces = 0
    for row in game_board:
        for piece in row:
            if piece == 1:
                p1_pieces += 1
            elif piece == 2:
                p2_pieces += 1

    if p1_pieces > p2_pieces:
        return 1
    elif p2_pieces > p1_pieces:
        return 2
    else:
        return 0
