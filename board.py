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

        # bind cells to be a cell object that is 9 rows x 9 col on screen
        self.cells = [
            [Cell(self.board[i][j], i, j, screen) for j in range(9)]
            for i in range(9)
        ]


    def draw(self):
        self.screen.fill(BG_COLOR)
        # we will be giving coloring in the board background
        for i in range(1, BOARD_ROWS + 1):
            # we will be drawing our horizontal lines that make up the cells on the board
            if i % 3 != 0:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH_CELL
                )
                # make the horizontal lines that will make up the boxes that will contain the cells on the board
            else:
                pygame.draw.line(
                    self.screen,
                    LINE_COLOR,
                    (0, i * SQUARE_SIZE),
                    (WIDTH, i * SQUARE_SIZE),
                    LINE_WIDTH_BOLD
                )

        # draw vertical lines (same process just done with for vertical lines onfthe board )
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
        # go to the list of cells and then draw the value in the cells on screen
        for i in self.cells:
            for j in i:
                j.draw(self.screen)


        button_font = pygame.font.Font(None, 40)

        reset_text = button_font.render("Reset", True, BUTTON_TEXT_COLOR)
        restart_text = button_font.render("Restart", True, BUTTON_TEXT_COLOR)
        exit_text = button_font.render("Exit", True, BUTTON_TEXT_COLOR)

        # button background color and text
        reset_surf = pygame.Surface((reset_text.get_size()[0] + 20, reset_text.get_size()[1] + 20))
        reset_surf.fill(BG_BUTTON_COLOR)
        reset_surf.blit(reset_text, (10, 10))
        restart_surf = pygame.Surface((restart_text.get_size()[0] + 20, restart_text.get_size()[1] + 20))
        restart_surf.fill(BG_BUTTON_COLOR)
        restart_surf.blit(restart_text, (10, 10))
        exit_surf = pygame.Surface((exit_text.get_size()[0] + 20, exit_text.get_size()[1] + 20))
        exit_surf.fill(BG_BUTTON_COLOR)
        exit_surf.blit(exit_text, (10, 10))

        # button rectangle ('easy','medium','hard')
        reset_rect = reset_surf.get_rect(
            center=(WIDTH // 2 - 200, HEIGHT // 2 + 450))
        restart_rect = restart_surf.get_rect(
            center=(WIDTH // 2, HEIGHT // 2 + 450))
        exit_rect = exit_surf.get_rect(
            center=(WIDTH // 2 + 200, HEIGHT // 2 + 450))

        # Draw buttons onto the screen
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



    def check_board(self):
        # check to see that the sudoku board is solved completely
        for i in range(9):
            for j in range(9):
                if self.board[i][j] != self.filled[i][j]:
                    return False
        return True

