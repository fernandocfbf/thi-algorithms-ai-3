from src.classes.Astart import Astar
from src.classes.Puzzle import Puzzle
from src.constants.board import INPUT_BOARD
from src.utils.heuristic import find_goal_position


def solve():
    y,x = find_goal_position(0, INPUT_BOARD)
    state = Puzzle(
        x=x,
        y=y,
        board=INPUT_BOARD,
        last_moviment="")
    algorithm = Astar()
    result = algorithm.search(state)
    if result != None:
        print(result.show_path())
        return 
    else:
        print("No solution found!")
        return

if __name__ == "__main__":
    solve()