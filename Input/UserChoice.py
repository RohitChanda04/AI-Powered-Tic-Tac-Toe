from Board import ShowBoard
from IPython.display import clear_output

def user_choice(test_board):
    p1 = input('\nChoose your sign "x" or "o": ').lower()
    if p1 not in ['x','X','o','O']:
        while p1 not in ['x','X','o','O']:
            clear_output()
            #ShowBoard.show_board(test_board)
            print('\nInvalid input! Please choose from "x" and "o".')
            p1 = input('\nChoose your sign "x" or "o": ').lower()
    p2 = ''
    if p1 == 'x':
        p2 = 'o'
    else:
        p2 = 'x'
    # print('\nPlayer 1, you have chosen "{}".'.format(p1))
    # print('\nPlayer 2, you are "{}".'.format(p2))
    return (p1, p2)