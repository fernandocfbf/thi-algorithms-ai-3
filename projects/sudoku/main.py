from src.classes.Reader import Reader
from src.classes.Sudoku import Sudoku
from src.classes.DFS import DFS

from src.utils.board import board_to_string

if __name__ == "__main__":
    reader = Reader()
    txt = reader.read_text_file('./src/data/sudoku1')
    board = reader.txt_to_matrix(txt)
    print("Sudoku to solve:")
    print(board_to_string(board))
    sudoku = Sudoku(board)
    dfs = DFS(sudoku)
    dfs.search()