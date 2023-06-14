## Sudoku Solver using Depth-First Search

This repository contains an implementation of a Sudoku solver using the depth-first search (DFS) technique. The Sudoku solver is designed to solve any valid Sudoku puzzle by systematically exploring the possible solutions until a valid solution is found.

### Introduction

Sudoku is a popular number puzzle game that involves filling a 9x9 grid with digits so that each column, each row, and each of the nine 3x3 subgrids contains all of the digits from 1 to 9 without repetition. Solving Sudoku puzzles can be a challenging task, requiring logical deduction and careful elimination of possibilities.

This repository provides a Sudoku solver that uses the depth-first search algorithm to solve Sudoku puzzles. The depth-first search algorithm explores the search space by systematically trying out each possible digit at each empty cell and backtracking when an invalid state is encountered. This approach guarantees finding a solution if one exists, or determining that the puzzle is unsolvable.

### Features

- Solves Sudoku puzzles of any difficulty level.
- Uses the depth-first search technique for exploring the solution space.
- Provides clear and concise code with appropriate documentation.
- Supports input of Sudoku puzzles as 9x9 grids using numbers inside a txt file.
- Displays the solved Sudoku puzzle as output.
- Includes sample puzzles for testing and demonstration.

### Usage

To use the Sudoku solver, follow these steps:

1. Open the `/src/data/sudoku1.txt` file.

2. Modify the `grid` variable to represent the Sudoku puzzle you want to solve. Use numbers from 1 to 9 to represent known values and use the number 0 for unknown values.

3. Run the program:

   ```
   python main.py
   ```

4. The solved Sudoku puzzle will be displayed in the console output.

Feel free to experiment with different Sudoku puzzles and see the solver in action!