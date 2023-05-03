import math
from AIPath import MiniMax

def bestPosition(board,jared,player) : 
    bestValue = (-1)*math.inf
    position = -1
    for i in range(9):
        if (board[i] == ' ') : 
            board[i] = jared
            score = MiniMax.mini_max(board, 0, False, jared, player) 
            board[i] = ' ' 
            if (score > bestValue):
                bestValue = score
                position = i
    return position