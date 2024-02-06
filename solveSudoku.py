import random

import numpy as np
from random import sample
from random import shuffle


class Solver:
    def __init__(self):
        # size of the 2d matrix/sudoku board
        self.n = 9

        self.board = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0]
        ]



    def debug(self):
        print(np.matrix(self.board))

    def generate_puzzle(self, grid):
        self.solve(grid)
        squares = self.n*self.n
        remove = squares * 3 // 4
        for i in sample(range(squares), remove):
            grid[i//self.n][i%self.n] = 0
        return grid


    def solve(self, grid, row = 0, col = 0):
        # if row value is such that the function has run its course, break
        if row == self.n:
            return True
        # if on the last cell of the column, move to the next row
        elif col == self.n:
            return self.solve(grid, row + 1, 0)
        # if at some other coordinate, move to the next cell
        elif grid[row][col] != 0:
            return self.solve(grid, row, col + 1)
        # if the cell is empty
        else:
            nums = list(range(1,10))
            random.shuffle(nums)
            # for every possible value a cell can hold 1-9
            for num in nums:
                # if that value is valid at the position, place it
                if self.valid(grid, row, col, num):
                    # print(np.matrix(board))
                    grid[row][col] = num
                    # if placing number at this cell eventually leads to a solution return true
                    if self.solve(grid, row, col + 1):
                        return True
                    # else empty the cell and try something else on next iteration
                    grid[row][col] = 0
            # no solution
            return False


    # function to check if 1 specific square (grid[row][col]) can contain value num legit
    def valid(self, grid, row, col, num):
        in_row = num in grid[row]
        in_column = num in [grid[r][col] for r in range(self.n)]
        if in_row or in_column:
            return False
        # get first cells in subgrid
        row_first_cell, column_first_cell = self.get_subgrid_starting_cells(row, col)
        # get last cells
        row_last_cell = row_first_cell + 3
        column_last_cell = column_first_cell + 3
        for r in range(row_first_cell, row_last_cell):
            for c in range(column_first_cell, column_last_cell):
                # if num is already in subgrid return false
                if grid[r][c] == num:
                    return False
        return True


    def get_subgrid_starting_cells(self, row, col):
        return row // 3 * 3, col // 3 * 3

solver = Solver()
# solver.debug()
# solver.solve(solver.board)
# solver.debug()





