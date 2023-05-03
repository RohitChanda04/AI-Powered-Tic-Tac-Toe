def heuristic_function(test_board,player,jared):

    #checking rows
    for i in range(0,7,3):
        if test_board[i] == test_board[i+1] == test_board[i+2] == jared:
            return 10
        elif test_board[i] == test_board[i+1] == test_board[i+2] == player:
            return (-10)
    
    #checking for columns
    for i in range(0,3):
        if test_board[i] == test_board[i+3] == test_board[i+6] == jared:
            return 0+10
        elif test_board[i] == test_board[i+3] == test_board[i+6] == player:
            return (-10)
        
    #checking for diagonal 1-5-9
    if test_board[0] == test_board[4] == test_board[8] == jared:
        return 0+10
    elif test_board[0] == test_board[4] == test_board[8] == player:
        return (-10)
    
    #checking for diagonal 3-5-7
    if test_board[2] == test_board[4] == test_board[6] == jared:
        return 0+10
    elif test_board[2] == test_board[4] == test_board[6] == player:
        return 0-10
    
    return 0