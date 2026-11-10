from validation import get_num_1_to_9

def show_board(board: list) -> str:
    return  f"""[1] {board[0] if board[0] else ' '} |[2] {board[1] if board[1] else ' '} |[3] {board[2] if board[2] else ' '}   
[4] {board[3] if board[3] else ' '} |[5] {board[4] if board[4] else ' '} |[6] {board[5] if board[5] else ' '}   
[7] {board[6] if board[6] else ' '} |[8] {board[7] if board[7] else ' '} |[9] {board[8] if board[8] else ' '}  
"""


def show_menu(turn_of: str) -> str:
    choice = get_num_1_to_9(f'The turn of {turn_of}! Enter cell number(1-9):')
    return choice - 1