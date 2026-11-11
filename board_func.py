def add_cell(board: list, cell_num: int, turn_of: str) -> str:
    board[cell_num] = turn_of
    return 'The selection has been saved!\n'


def check_if_win(board: list, type: str) -> bool:
    WINNING_LINES = [
    (0, 1, 2),
    (3, 4, 5),
    (6, 7, 8),
    (0, 3, 6),
    (1, 4, 7),
    (2, 5, 8),
    (0, 4, 8),
    (2, 4, 6),
    ]
    
    for line in WINNING_LINES:
        if board[line[0]]\
        == board[line[1]]\
        == board[line[2]] == type:
            return True
        
    return False



def check_if_draw(board: list) -> bool:
    result = list(filter(lambda c: c is None, board))
    return False if result else True