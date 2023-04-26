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
        self.OG, self.solution = generate_sudoku(BOARD_SIZE, difficulty)
        self.pos = (0, 0)

        # Fill my board
        self.board = [[None] * BOARD_SIZE for i in range(BOARD_SIZE)]
        for current_row in range(len(self.OG)):
            for current_col in range(len(self.OG[0])):
                self.board[current_row][current_col] = Cell(self.OG[current_row][current_col],
                                                            current_row,
                                                            current_col,
                                                            self.solution[current_row][current_col]
                                                            == self.OG[current_row][current_col])


    def draw(self):

        self.screen.fill(BG_COLOR)
        # fill in the background color
        for i in range(10):
            # draw the vert lines that will make the cells
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (i * CELL_D, 0),
                (i * CELL_D, BOTTOM_B),
                LINE_WIDTH_CELL
            )
            # draw the horz lines that will make the cells
            pygame.draw.line(
                self.screen,
                LINE_COLOR,
                (0,i * CELL_D ),
                (self.width, i * CELL_D),
                LINE_WIDTH_CELL
            )
        for i in range(4):
            # draw the vert lines in bold that will create the border of the boxes
            pygame.game.draw.line(
                self.screen,
                LINE_COLOR,
                (i * BOX_D, 0),
                (i * BOX_D, BOTTOM_B),
                LINE_WIDTH_BOLD
            )
            # draw the horz line in bold that will create the border of the boxes
            pygame.game.draw.line(
                self.screen,
                LINE_COLOR,
                (0, i *BOX_D),
                (self.width, i * BOX_D),
                LINE_WIDTH_BOLD
            )
        [[j.draw() for j in i] for i in self.board]
        # here we draw each cell
    def select(self, row, col):
        # mark the cell at position in the board that will be the current selected cell
        # a selected cell can then have its value change
        self.board[self.pos[0]][self.pos[1]].selected = False
        self.pos = (row,col)
        self.board[self.pos[0]][self.pos[1]].selected = True

    def click(self, x, y):
        # a tuple of (x, y) coordinates is returned if those that position is within the board,
        # the position corresponds to the cell that is clicked

        if y > BOTTOM_B:
            return (False, None, None)
        else:
            return (True, y // CELL_D, x // CELL_D)

    def clear(self):
        # clear the value of the cell, the user can remove values and sketched value that are filled by themselves
        current_row, current_col = self.pos
        if self.OG[current_row][current_col] != self.board[current_row][current_col].value:
            self.board[current_row][current_col].set_cell_value(0)
        self.board[current_row][current_col].set_sketched_value(0)


    def sketch(self, value):
        # set the sketched value of the current cell == user entered value
        # the sketched value will be displayed in the top left corner of the cell using the draw() fun
        current_row, current_col = self.pos
        if not self.board[current_row][current_col].is_OG:
            self.board[current_row][current_col].set_sketched_value(value)


    def place_number(self, value):
        # set the value of the current selected cell == to the user input
        # called when the user used the 'ENTER' key
        current_row, current_col = self.pos
        if not self.board[current_row][current_col].is_OG:
            if self.board[current_row][current_col].sketched_value != 0:
                self.board[current_row][current_col].set_cell_value(self.board[current_row][current_col].sketched_value)
                self.board[current_row][current_col].set_sketched_value(0)


    def reset_to_original(self):
        # reset the cells in the board to OG values (0 if cleared, else: corresponding to digit)
        for i in range(len(self.OG)):
            for j in range(len(self.OG[0])):
                [self.board[i][j].set_cell_value(self.OG[i][j])]
                [self.board[i][j].set_sketched_value(self.OG[i][j])]

    def is_full(self):
        # return Boolean corresponding to whether the board is full or not
        for i in range(len(self.OG)):
            for j in range(len(self.OG[0])):
                if self.board[i][j].value == 0:
                    return False
        return True

    def update_board(self):
        #update the 2d board w/ the values in all cells
        for i in range[BOARD_SIZE]:
            for j in range[BOARD_SIZE]:
                self.board[i][j].value = self.board[i][j].temp_value

    def find_empty(self):
        # find an empty cell and return the row and col as a tuple (row,col)
        # is this needed? i don't know
        for col in range[BOARD_SIZE]:
            for row in range[BOARD_SIZE]:
                if self.board[row][col] == 0:
                    return (row, col)
        return None

    def check_board(self):
        # check to see that the sudoku board is solved completely
        for i in range(len(self.)):
            for j in range(len(self.OG[0])):
                if self.board[i][j].value != self.solution[i][j]:
                    return False
        return True


