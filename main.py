import time
from output import show_board, show_menu
from validation import check_cell
from board_func import add_cell, check_if_win, check_if_draw

board = [None for n in range(9)]
turn_of = 'x'

if __name__ == '__main__':
    while True:
        print(show_board(board))
        
        cell_num = show_menu(turn_of)
        
        if check_cell(board, cell_num):
            print('The cell already full!')
            continue
        
        print(add_cell(board, cell_num, turn_of))
        
        
        if check_if_win(board, turn_of):
            print(show_board(board), f'Player {turn_of} WIN!')
            break
        
        if check_if_draw(board):
            print(show_board(board), 'Its a draw!')
            break
            
        
        turn_of = 'o' if turn_of == 'x' else 'x'
        
        
        time.sleep(2)
        
        