from src.classes.Board import Board
from src.constants.knight import MOVES

class Knight():
    def __init__(self, start_position, target_position, board_size):
        self.x = start_position[0]
        self.y = start_position[1]
        self.target_x = target_position[0]
        self.target_y = target_position[1]
        self.board = Board(width=board_size, height=board_size)
        self.board.initialize_board()
    
    def is_valid_movement(self, x, y):
        is_valid_x_position = (x >= 0 and x < 8)
        is_valid_y_position = (y >= 0 and y < 8)
        return is_valid_x_position and is_valid_y_position
    
    def get_possible_moves(self):
        all_possible_moviments = list()
        for moviment in MOVES:
            next_position = [self.x + moviment[0], self.y + moviment[1]]
            if self.is_valid_movement(next_position[0], next_position[1]):
                all_possible_moviments.append(next_position)
        return all_possible_moviments

