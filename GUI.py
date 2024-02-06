from solveSudoku import Solver
import pygame as pg
import os
import sys
import copy


class SudokuGUI:
    def __init__(self):
        pg.init()
        self.screen_size = (550, 550)
        self.screen = pg.display.set_mode(self.screen_size)
        pg.display.set_caption("Sudoku")
        self.clock = pg.time.Clock()
        self.screen.fill(pg.Color("white"))
        self.solver = Solver()
        self.font = pg.font.SysFont('Century Gothic', 35)
        self.board = self.solver.generate_puzzle(self.solver.board)
        self.og_puzzle = copy.deepcopy(self.board)
        self.selected_pos = None
        self.play_music()

    def find_music_path(self):
        app_folder = os.path.dirname(os.path.realpath(sys.argv[0]))
        p = os.path.join(app_folder, "sudoku_music.ogg")
        return p

    def input(self, screen, position):
        print(f"Input function called with position: {position}")
        i, j = position[1], position[0]
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return
                if event.type == pg.KEYDOWN:
                    if self.og_puzzle[i-1][j-1] != 0:
                        return  # Exit if the cell is not editable
                    if (event.key == 48):  # 0 key
                        print("0 was pressed")
                        self.board[i-1][j-1] = 0
                        pg.draw.rect(screen, 'white', (j * 50 + 5, i * 50 + 10, 50 - 10, 50 - 10))
                        pg.display.update()
                        return
                    if (0 < event.key - 48 < 10):  # any other valid input
                        print("key was pressed")
                        self.board[i-1][j-1] = event.key - 48
                        pg.draw.rect(screen, 'white', (j * 50 + 5, i * 50 + 10, 50 - 10, 50 - 10))
                        value = self.font.render(str(event.key - 48), True, 'black')
                        screen.blit(value, (position[0] * 50 + 15, position[1] * 50 + 5))
                        pg.display.update()
                        if event.key - 48 != self.solver.solved_board[i-1][j-1]:
                            print("Incorrect")
                        else:
                            print("Correct")
                        return


    def play_music(self):
        pg.mixer.init()
        song = self.find_music_path()
        pg.mixer.music.load(song)
        pg.mixer.music.play(-1, 0, 0)

    # Creates grid
    def draw_board(self):
        for i in range(0, self.solver.n + 1):
            width = 4 if i % 3 == 0 else 2
            pg.draw.line(self.screen, (0, 0, 0), (50 + 50 * i, 50), (50 + 50 * i, 500), width)
            pg.draw.line(self.screen, (0, 0, 0), (50, 50 + 50 * i), (500, 50 + 50 * i), width)
        pg.display.update()

    def print_values(self, grid):
        for i in range(self.solver.n):
            for j in range(self.solver.n):
                if grid[i][j] != 0:
                    # render number to print
                    value = self.font.render(str(grid[i][j]), True, 'black')
                    # print it to screen at x, y coordinate
                    self.screen.blit(value, ((j + 1) * 50 + 15, (i + 1) * 50 + 5))
        pg.display.update()

    def main(self):
        running = True
        while running:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONUP and event.button == 1:
                    pos = pg.mouse.get_pos()
                    self.selected_pos = (pos[0] // 50, pos[1] // 50)
                    self.input(self.screen, self.selected_pos)
                if event.type == pg.QUIT:
                    running = False

            self.draw_board()
            self.print_values(self.board)
            # self.print_values()
            pg.display.flip()
            self.clock.tick(60)
        pg.quit()


if __name__ == '__main__':
    sudokuGUI = SudokuGUI()
    sudokuGUI.main()
