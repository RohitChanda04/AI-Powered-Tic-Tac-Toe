def vacant_positions(board):
    for i in range(9):
        if board[i] == ' ':
            return True
    return False