def find_goal_position(number, board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if int(board[i][j]) == int(number):
                return [i,j]