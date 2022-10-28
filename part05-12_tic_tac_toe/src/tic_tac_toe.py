def play_turn(game_board: list, x: int, y: int, piece: str):
    if x not in range(3) or y not in range(3) or game_board[y][x] != '':
        return False
    else:
        game_board[y][x] = piece
        return True
