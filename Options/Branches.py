import time
import math
import random
from Board import CheckPosition
from Board import CheckStatus
from Board import ShowBoard

from Input import UserChoice
from Input import UserInput

from Round import Turn
from Round import Update

from StartGame import TicTacToe
from AIPath import AITurn
from Game import ContinueGame

from IPython.display import clear_output


def ai_operated():
    '''
    This is the main funciton for AI-powered game.
    The user chooses his sign and then proceeds to say if he wants to go first.
    To check that, we have taken a variable called first.
    '''
    demo_board = ['1','2','3','4','5','6','7','8','9']
    test_board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']

    print('\nYou are playing against the AI-powered futuristic bot, Jared!\n')

    levelList1 = ['1','one','ONE','One','OnE','oNe','oNE','ONe','Beginner','beginner','BEGINNER']
    levelList2 = ['2','two','TWO','Two','TwO','tWo','tWO','TWo','Intermediate','intermediate','INTERMEDIATE']
    levelList3 = ['3','three','THREE','Three','tHree','thRee','thrEe','threE','Expert','expert','EXPERT']
    level = choose_level(levelList1, levelList2, levelList3)
    if level in levelList1:
        print('\nBeginner level selected!\n')
        beginner(test_board, demo_board)
        return
    elif level in levelList2:
        print('\nIntermediate level selected!\n')
        intermediate(test_board, demo_board)
        return
    else:
        print('\nExpert level selected!\n')
        expert(test_board, demo_board)



def beginner(test_board, demo_board):
    player, jared = UserChoice.user_choice(test_board)
    print()
    print('\nPlayer 1, you have chosen "{}".'.format(player))
    print('\nJared is "{}".'.format(jared))

    #setting the values of the variables tieFlag and first
    first = ''
    tieFlag = True
    first = input('\nDo you want to start first? ')
    while first not in ['Yes','Y','yes','y','YES'] and first not in ['No','N','no','n','NO']:
        print('\nInvalid input...\n')
        first = input('\nDo you want to start first? ')
    if first in ['Yes','Y','yes','y','YES']:
        first = 'y'
    else:
        first = 'n'

    print('\nEnter the position numbers corresponding to those in the board below...\n')
    ShowBoard.show_board(demo_board)
    print('\nOkay, so presenting the empty board now...\n')
    ShowBoard.show_board(test_board)

    #main loop of this game
    i = 0
    while i < len(test_board):

        if CheckStatus.check_status(jared,test_board):
            print("\nGame over! Jared wins!\n")
            tieFlag = False
            break

        if first == 'n':
            #Jared's turn...
            print('\n\nJared is playing...')
            vacantIndices = []
            index = 0
            while index in range(9):
                if test_board[index] == ' ':
                    vacantIndices.append(index)
                index += 1
            pos = random.choice(vacantIndices) + 1
            print()
            test_board = Update.update(test_board, pos, jared)
            ShowBoard.show_board(test_board)
            print('\n')
            first = ''
            i += 1
        
        if CheckStatus.check_status(jared,test_board):
            print("\nGame over! Jared wins!\n")
            tieFlag = False
            break

        #player's turn now...
        print("\nPlayer 1, it's your turn...")
        position = UserInput.user_input()
        while CheckPosition.check_position(test_board,position):
            print('\nPosition {} is already filled, choose something else!'.format(position))
            position = UserInput.user_input()
        clear_output()
        test_board = Turn.turn(test_board,position,player)
        print('\n')
        ShowBoard.show_board(test_board)
        print()
        i += 1
        if CheckStatus.check_status(player,test_board):
            print("\nGame over! You win!\n")
            tieFlag = False
            break

        if CheckStatus.check_status(jared,test_board):
            print("\nGame over! Jared wins!\n")
            tieFlag = False
            break

        #Jared's turn...
        print('\nJared is playing...')
        vacantIndices = []
        index = 0
        while index in range(9):
            if test_board[index] == ' ':
                vacantIndices.append(index)
            index += 1
        pos = random.choice(vacantIndices) + 1
        print()
        test_board = Update.update(test_board, pos, jared)
        ShowBoard.show_board(test_board)
        print('\n')
        # if not tieFlag:
        #         break
        i += 1


    if tieFlag:
        print("\nTie!!!\n")
    if ContinueGame.continue_game():
        TicTacToe.tic_tac_toe()
    else:
        print('\nThank you for playing, have a great day!\n')



def intermediate(test_board, demo_board):
    player, jared = UserChoice.user_choice(test_board)
    print()
    print('\nPlayer 1, you have chosen "{}".'.format(player))
    print('\nJared is "{}".'.format(jared))

    #setting the values of the variables tieFlag and first
    first = ''
    tieFlag = True
    randomList = [True,False]
    first = input('\nDo you want to start first? ')
    while first not in ['Yes','Y','yes','y','YES'] and first not in ['No','N','no','n','NO']:
        print('\nInvalid input...\n')
        first = input('\nDo you want to start first? ')
    if first in ['Yes','Y','yes','y','YES']:
        first = 'y'
    else:
        first = 'n'

    print('\nEnter the position numbers corresponding to those in the board below...\n')
    ShowBoard.show_board(demo_board)
    print('\nOkay, so presenting the empty board now...\n')
    ShowBoard.show_board(test_board)

    #main loop of this game
    i = 0
    while i < len(test_board):

        if CheckStatus.check_status(jared,test_board):
            print("\nGame over! Jared wins!\n")
            tieFlag = False
            break

        if first == 'n':
            #Jared's turn...
            randomChoice = random.choice(randomList)
            if randomChoice:
                print('\n\nJared is playing...')
                vacantIndices = []
                index = 0
                while index in range(9):
                    if test_board[index] == ' ':
                        vacantIndices.append(index)
                    index += 1
                pos = random.choice(vacantIndices) + 1
                test_board = Update.update(test_board, pos, jared)
            else:
                test_board, tieFlag = AITurn.ai_turn(test_board,player,jared,tieFlag)
            print()
            ShowBoard.show_board(test_board)
            print('\n')
            first = ''
            i += 1
        
        if CheckStatus.check_status(jared,test_board):
            print("\nGame over! Jared wins!\n")
            tieFlag = False
            break

        #player's turn now...
        print("\nPlayer 1, it's your turn...")
        position = UserInput.user_input()
        while CheckPosition.check_position(test_board,position):
            print('\nPosition {} is already filled, choose something else!'.format(position))
            position = UserInput.user_input()
        clear_output()
        test_board = Turn.turn(test_board,position,player)
        ShowBoard.show_board(test_board)
        i += 1

        if CheckStatus.check_status(player,test_board):
            print("\nGame over! You win!\n")
            tieFlag = False
            break

        # if CheckStatus.check_status(jared,test_board):
        #     print("\nGame over! Jared wins!\n")
        #     tieFlag = False
        #     break

        #Jared's turn...
        randomChoice = random.choice(randomList)
        if randomChoice:
            print('\n\nJared is playing...')
            vacantIndices = []
            index = 0
            while index in range(9):
                if test_board[index] == ' ':
                    vacantIndices.append(index)
                index += 1
            pos = random.choice(vacantIndices) + 1
            test_board = Update.update(test_board, pos, jared)
        else:
            test_board, tieFlag = AITurn.ai_turn(test_board,player,jared,tieFlag)
        print()
        ShowBoard.show_board(test_board)
        print('\n')
        i += 1


    if tieFlag:
        print("\nTie!!!\n")
    if ContinueGame.continue_game():
        TicTacToe.tic_tac_toe()
    else:
        print('\nThank you for playing, have a great day!\n')



def expert(test_board, demo_board):
    player, jared = UserChoice.user_choice(test_board)
    print()
    print('\nPlayer 1, you have chosen "{}".'.format(player))
    print('\nJared is "{}".'.format(jared))

    #setting the values of the variables tieFlag and first
    first = ''
    tieFlag = True
    first = input('\nDo you want to start first? ')
    while first not in ['Yes','Y','yes','y','YES'] and first not in ['No','N','no','n','NO']:
        print('\nInvalid input...\n')
        first = input('\nDo you want to start first? ')
    if first in ['Yes','Y','yes','y','YES']:
        first = 'y'
    else:
        first = 'n'

    print('\nEnter the position numbers corresponding to those in the board below...\n')
    ShowBoard.show_board(demo_board)
    print('\nOkay, so presenting the empty board now...\n')
    ShowBoard.show_board(test_board)

    #main loop of this game
    i = 0
    while i < len(test_board):

        if CheckStatus.check_status(jared,test_board):
            print("\nGame over! Jared wins!\n")
            tieFlag = False
            break

        if first == 'n':
            #Jared's turn...
            test_board, tieFlag = AITurn.ai_turn(test_board,player,jared,tieFlag)
            ShowBoard.show_board(test_board)
            
            first = ''
            i += 1
        
        if CheckStatus.check_status(jared,test_board):
            print("\nGame over! Jared wins!\n")
            tieFlag = False
            break

        #player's turn now...
        print("\nPlayer 1, it's your turn...")
        position = UserInput.user_input()
        while CheckPosition.check_position(test_board,position):
            print('\nPosition {} is already filled, choose something else!'.format(position))
            position = UserInput.user_input()
        clear_output()
        test_board = Turn.turn(test_board,position,player)
        ShowBoard.show_board(test_board)
        i += 1
        if CheckStatus.check_status(player,test_board):
            print("\nGame over! You win!\n")
            tieFlag = False
            break

        # if CheckStatus.check_status(jared,test_board):
        #     print("\nGame over! Jared wins!\n")
        #     tieFlag = False
        #     break

        #Jared's turn...
        test_board, tieFlag = AITurn.ai_turn(test_board,player,jared,tieFlag)
        ShowBoard.show_board(test_board)
        i += 1


    if tieFlag:
        print("\nTie!!!\n")
    if ContinueGame.continue_game():
        TicTacToe.tic_tac_toe()
    else:
        print('\nThank you for playing, have a great day!\n')



def choose_level(levelList1, levelList2, levelList3):
	level = input('\nChoose the difficulty level: \n1. Beginner \n2. Intermediate \n3. Expert \n\n')
	while level not in levelList1 and level not in levelList2 and level not in levelList3:
		print('\nEnter a valid option...')
		level = input('\nChoose the difficulty level: \n1. Beginner \n2. Intermediate \n3. Expert \n\n')
	return level