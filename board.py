# this class represents an entire Sudoku board
from cell import Cell
from sudoku_generator import *
from constants import *
import pygame


class Board:
    # this class containing 81 cells
    def __init__(self, width, height, screen, difficulty):
        # constructor for the board class
        # screen will be the window from pygame
        # easy, med, hard will be the variable decided by user
        # (corresponding with the number of empty cells, 30,40,50 respectively)
        self.width = width
        self.height = height
        self.screen = screen
        self.difficulty = difficulty
        self.board, self.filled, self.OG = generate_sudoku(BOARD_SIZE, difficulty)
        #self.filled = generate_sudoku(BOARD_SIZE, difficulty)
        #self.OG = generate_sudoku(BOARD_SIZE, difficulty)
        #self.OG = generate_sudoku(BOARD_SIZE, difficulty)
        #self.filled = generate_sudoku(BOARD_SIZE, difficulty)

        # bind cells to be a cell object that is 9 rows x 9 col on screen
        self.cells = [
            [Cell(self.board[i][j], i, j, screen) for j in range(9)]
            for i in range(9)
        ]


    def draw(self):
        self.screen.fill(BG_COLOR)
        for i in range(1, BOARD_ROWS + 1):
            if i % 3 != 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH_CELL
                )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH_BOLD
                )

        # draw vertical lines
        for j in range(1, BOARD_COLS):
            if j % 3 != 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0),
                    (j * SQUARE_SIZE, HEIGHT - (HEIGHT - WIDTH)),
                    LINE_WIDTH_CELL
                )
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (j * SQUARE_SIZE, 0),
                    (j * SQUARE_SIZE, HEIGHT - (HEIGHT - WIDTH)),
                    LINE_WIDTH_BOLD
                )
        # This for loop goes through each cell in the list of cell objects and draws each individual cells
        for i in self.cells:
            for j in i:
                j.draw(self.screen)


        button_font = pygame.font.Font(None, 40)

        reset_text = button_font.render("Reset", True, BUTTON_COLOR)
        restart_text = button_font.render("Restart", True, BUTTON_COLOR)
        exit_text = button_font.render("Exit", True, BUTTON_COLOR)

        # Initialize button background color and text
        reset_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surf.fill(LINE_COLOR)
        reset_surf.blit(reset_text, (10, 10))
        restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surf.fill(LINE_COLOR)
        restart_surf.blit(restart_text, (10, 10))
        exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surf.fill(LINE_COLOR)
        exit_surf.blit(exit_text, (10, 10))

        # Initialize button rectangle
        reset_rect = reset_surf.get_rect(
            center=(WIDTH // 2 - 200, HEIGHT // 2 + 450))
        restart_rect = restart_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 450))
        exit_rect = exit_surf.get_rect(
            center=(WIDTH // 2 + 200, HEIGHT // 2 + 450))

        # Draw buttons
        self.screen.blit(reset_surf, reset_rect)
        self.screen.blit(restart_surf, restart_rect)
        self.screen.blit(exit_surf, exit_rect)

        return reset_rect, restart_rect, exit_rect

    def select(self, row, col):
        # mark the cell at position in the board that will be the current selected cell
        # a selected cell can then have its value change
        for i in self.cells:
            for j in i:
                if j.row == row and j.col == col:
                    j.selected = True
                    return j

    def click(self, x, y):
        # a tuple of (x, y) coordinates is returned if those that position is within the board,
        # the position corresponds to the cell that is clicked

        row = x // SQUARE_SIZE
        col = y // SQUARE_SIZE
        return row, col

    #def clear(self):
    #    # clear the value of the cell, the user can remove values and sketched value that are filled by themselves
    #    current_row, current_col = self.pos
    #    if self.OG[current_row][current_col] != self.board[current_row][current_col].value:
    #        self.board[current_row][current_col].set_cell_value(0)
    #    self.board[current_row][current_col].set_sketched_value(0)


    #def sketch(self, value):
    #    # set the sketched value of the current cell == user entered value
    #    # the sketched value will be displayed in the top left corner of the cell using the draw() fun
    #    current_row, current_col = self.pos
    #    if not self.board[current_row][current_col].is_OG:
    #        self.board[current_row][current_col].set_sketched_value(value)


    #def place_number(self, value):
    #    # set the value of the current selected cell == to the user input
    #    # called when the user used the 'ENTER' key
    #    current_row, current_col = self.pos
    #    if not self.board[current_row][current_col].is_OG:
    #        if self.board[current_row][current_col].sketched_value != 0:
    #            self.board[current_row][current_col].set_cell_value(self.board[current_row][current_col].sketched_value)
    #            self.board[current_row][current_col].set_sketched_value(0)


    def reset_to_original(self):
        # reset the cells in the board to OG values (0 if cleared, else: corresponding to digit)
        for i in range(9):
            for j in range(9):
                self.board[i][j] = self.OG[i][j]
                (self.cells[i][j]).value = self.board[i][j]
        self.update_board()
        self.draw()

    def is_full(self):
        # return Boolean corresponding to whether the board is full or not
        for i in self.board:
            for j in i:
                if j == 0:
                    return False
        return True

    def update_board(self):
        #update the 2d board w/ the values in all cells
        for i in self.cells:
            for j in i:
                self.board[j.row][j.col] = j.value

    #def find_empty(self):
    #    # find an empty cell and return the row and col as a tuple (row,col)
        # is this needed? i don't know
    #    for col in range[BOARD_SIZE]:
    #        for row in range[BOARD_SIZE]:
    #            if self.board[row][col] == 0:
    #                return (row, col)
    #    return None

    def check_board(self):
        # check to see that the sudoku board is solved completely
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.filled[i][j]:
                    return False
        return True
        #for i in range(len(self.OG)):
        #    for j in range(len(self.OG[0])):
        #        if self.board[i][j].value != self.solution[i][j]:
        #            return False
        #return True


