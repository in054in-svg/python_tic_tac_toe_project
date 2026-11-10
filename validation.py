def get_num_1_to_9(message: str) -> int:
    try:
        choice = int(input(message))
        if choice in [1,2,3,4,5,6,7,8,9]:
            return choice
        print('Enter number between 1-9 only!')
    except ValueError:
        print('Enter numbers only!')
        

def check_cell(board: list, cell_num) -> bool:
    return board[cell_num]