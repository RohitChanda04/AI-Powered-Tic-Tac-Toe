def show_board(board):
    for i in range(0,len(board)):
        print(' '+board[i]+' ',end = '')
        if (i+1) % 3 != 0:
            print('|',end = '')
        else:
            print()
            if i != len(board)-1:
                print('-----------')