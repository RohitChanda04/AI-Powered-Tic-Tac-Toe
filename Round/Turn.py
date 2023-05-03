from Round import Update

def turn(board,position,sign):
    board = Update.update(board,position,sign)
    return board