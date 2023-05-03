def check_status(sign,test_board):
    if test_board[0] == test_board[1] == test_board[2] == sign:
        return True
    elif test_board[0] == test_board[4] == test_board[8] == sign:
        return True
    elif test_board[0] == test_board[3] == test_board[6] == sign:
        return True
    elif test_board[2] == test_board[4] == test_board[6] == sign:
        return True
    elif test_board[2] == test_board[5] == test_board[8] == sign:
        return True
    elif test_board[1] == test_board[4] == test_board[7] == sign:
        return True
    elif test_board[3] == test_board[4] == test_board[5] == sign:
        return True
    elif test_board[6] == test_board[7] == test_board[8] == sign:
        return True
    else:
        return False