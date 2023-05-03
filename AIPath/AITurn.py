import time
from Board import CheckStatus

from Round import Update

from AIPath import BestPosition

from IPython.display import clear_output

def ai_turn(test_board, player, jared, tieFlag):
    if CheckStatus.check_status(jared, test_board):
        print("\nGame over! Jared wins!\n")
        tieFlag = False
        return (test_board, tieFlag)
    
    print("\n\nJared is playing...")

    position = BestPosition.bestPosition(test_board, jared, player) + 1
    test_board = Update.update(test_board, position, jared)
    return (test_board, tieFlag)