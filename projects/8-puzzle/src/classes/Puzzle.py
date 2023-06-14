from copy import deepcopy

from src.utils.heuristic import find_goal_position
from src.constants.moviments import POSSIBLE_MOVIMENTS, MOVIMENTS_DESCRIPTION
from src.constants.board import GOAL_BOARD

class Puzzle():
    def __init__(self, x, y, board, last_moviment):
        self.x = x
        self.y = y
        self.board = board
        self.last_moviment = last_moviment
    
    def env(self):
        return "{0}".format(self.board)
    
    def is_goal(self):
        return self.board == GOAL_BOARD
    
    def switch(self, board, cx, cy):
        res = deepcopy(board)
        res[self.y][self.x] = res[cy][cx]
        res[cy][cx] = 0
        return res
    
    def is_valid_moviment(self,x,y):
        return (y < 3 and y >= 0) and (x < 3 and x >= 0)

    def sucessors(self):
        childrens = list()
        for possibility in POSSIBLE_MOVIMENTS:
            y_position = self.y + possibility[1]
            x_position = self.x + possibility[0]
            if self.is_valid_moviment(x_position, y_position):
                current_board_state = deepcopy(self.board)
                next_board_state = self.switch(current_board_state, x_position, y_position)
                moviment = MOVIMENTS_DESCRIPTION[tuple(possibility)]
                childrens.append(Puzzle(x_position, y_position, next_board_state, moviment))
        return childrens

    def h(self):
        board_distance = 0
        for line in range(len(self.board)):
            for column in range(len(self.board)):
                number = str(self.board[line][column])
                goal_position = find_goal_position(number, GOAL_BOARD)
                distance = abs(line - goal_position[0]) + abs(column - goal_position[1])
                board_distance += distance
        return board_distance


