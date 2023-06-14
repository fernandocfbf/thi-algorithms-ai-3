class Board():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = None

    def initialize_board(self):
        board = list()
        row = [0]*self.width
        for i in range(self.height):
            board.append(row)
        self.board = board