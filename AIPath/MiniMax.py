import math
from AIPath import HeuristicFunction
from AIPath import VacantPositions

def mini_max(board, depth, isMax, jared, player): 
    score = HeuristicFunction.heuristic_function(board, player, jared)
  
    # If Maximizer has won the game return his/her evaluated score 
    if score == 10: 
        return score
  
    # If Minimizer has won the game return his/her evaluated score 
    if score == -10:
        return score
  
    # If there are no more moves and no winner then it is a tie
    if VacantPositions.vacant_positions(board) == False:
        return 0
  
    # If this maximizer's move 
    if isMax:     
        best = (-1)*math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = jared
                temp = mini_max(board, depth + 1, False, jared, player)
                board[i] = ' '
                best = max( best, temp)
        return best
  
    # If this minimizer's move 
    else:
        best = math.inf
        for i in range(9):
            if board[i] == ' ':
                board[i] = player
                temp = mini_max(board, depth + 1, True, jared, player)
                board[i] = ' '
                best = min(best, temp)
        return best