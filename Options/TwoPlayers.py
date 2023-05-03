from Board import CheckPosition
from Board import CheckStatus
from Board import ShowBoard

from Input import UserChoice
from Input import UserInput

from Round import Turn
from Round import Update

from StartGame import TicTacToe

from Game import ContinueGame

from IPython.display import clear_output

def two_players():
    demo_board = ['1','2','3','4','5','6','7','8','9']
    test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    print('\nYou are playing against another player!\n')
    print('\nEnter the position numbers corresponding to those in the board below...\n')
    ShowBoard.show_board(demo_board)
    print('\nOkay, so presenting the empty board now...\n')
    ShowBoard.show_board(test_board)

    print('\nPlayer 1...')
    p1, p2 = UserChoice.user_choice(test_board)
    print('\nPlayer 1, you have chosen "{}".'.format(p1))
    print('\nPlayer 2, you are "{}".'.format(p2))

    print()
    tieFlag = True
    i = 0

    while i < len(test_board):

        if i % 2 == 0:
            print("\nPlayer 1, it's your turn...")
            position = UserInput.user_input()
            while CheckPosition.check_position(test_board,position):
                print('\nPosition {} is already filled, choose something else!'.format(position))
                position = UserInput.user_input()
            clear_output()
            test_board = Turn.turn(test_board,position,p1)
            ShowBoard.show_board(test_board)
            i += 1
            if CheckStatus.check_status(p1,test_board):
                print("\nGame over! Player 1 wins!\n")
                tieFlag = False
                break
            else:
                continue
        
        if i % 2 != 0:
            print("\nPlayer 2, it's your turn...")
            position = UserInput.user_input()
            while CheckPosition.check_position(test_board,position):
                print('\nPosition {} is already filled, choose something else!'.format(position))
                position = UserInput.user_input()
            clear_output()
            test_board = Turn.turn(test_board,position,p2)
            ShowBoard.show_board(test_board)
            i += 1
            if CheckStatus.check_status(p2,test_board):
                print("\nGame over! Player 2 wins!\n")
                tieFlag = False
                break
            else:
                continue
    
    if tieFlag:
        print("\nTie!!!\n")
    if ContinueGame.continue_game():
        TicTacToe.tic_tac_toe()
    else:
        print('\nThank you for playing, have a great day!\n')