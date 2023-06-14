from copy import deepcopy

class Sudoku():
    def __init__(self, board, rows=9, cols=9):
        self.board = board
        self.rows = rows
        self.cols = cols

    def check_if_its_equal(self, other_puzzle):
        if isinstance(other_puzzle, Sudoku):
            return self.puzzle == other_puzzle.puzzle
        return self.puzzle == other_puzzle
    
    def check_valid_value_row(self, row, value):
        for col in range(self.cols):
            if self.board[row][col] == value:
                return False
        return True
    
    def check_valid_value_col(self, col, value):
        for row in range(self.rows):
            if self.board[row][col] == value:
                return False
        return True
    
    def check_valid_value_box(self, row, col, value):
        square_row_start = (row // 3) * 3
        square_col_start = (col // 3) * 3
        for row in range(square_row_start, square_row_start + 3):
            for col in range(square_col_start, square_col_start + 3):
                if self.board[row][col] == value:
                    return False
        return True
    
    def find_empty_slot(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    return (row, col)
        return None
    
    def extend_node(self):
        row, col = self.find_empty_slot()
        new_nodes = list()
        for value in range(1, 10):
            if self.check_valid_value_row(row, value) and self.check_valid_value_col(col, value) and self.check_valid_value_box(row, col, value):
                new_board = deepcopy(self.board)
                new_board[row][col] = value
                new_nodes.append(Sudoku(new_board))
        return new_nodes
    
    def is_solution(self):
        for row in range(self.rows):
            for col in range(self.cols):
                if self.board[row][col] == 0:
                    return False
        return True
    
    def to_string(self):
        sudoku = ""
        for row in range(self.rows):
            for col in range(self.cols):
                sudoku += f"{self.board[row][col]} "
            sudoku += "\n"
        return sudoku