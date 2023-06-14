def board_to_string(board):
    sudoku = ""
    for row in range(9):
        for col in range(9):
            sudoku += f"{board[row][col]} "
        sudoku += "\n"
    return sudoku