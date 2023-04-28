# this class represents a single cell in the sudoku board
from constants import *
import pygame

class Cell:
    def __init__(self, value, row, col, screen):
        # constructor for the cell class
        # value will be a number 0-9
        # instance attributes set up in the constructor
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.select = False




    def set_cell_value(self, value):
        # setter for the cell value
        self.value = value


    def draw(self, screen):
        # give the sudoku numbers their own font and size
        num_font = pygame.font.SysFont(NUM_FONT, NUM_SIZE)
        # Sets up the fonts and colors for each possible number on the board
        num0_surf = num_font.render('0', True, NUM_COLOR)
        num1_surf = num_font.render('1', True, NUM_COLOR)
        num2_surf = num_font.render('2', True, NUM_COLOR)
        num3_surf = num_font.render('3', True, NUM_COLOR)
        num4_surf = num_font.render('4', True, NUM_COLOR)
        num5_surf = num_font.render('5', True, NUM_COLOR)
        num6_surf = num_font.render('6', True, NUM_COLOR)
        num7_surf = num_font.render('7', True, NUM_COLOR)
        num8_surf = num_font.render('8', True, NUM_COLOR)
        num9_surf = num_font.render('9', True, NUM_COLOR)
        # This part make the outline of the cell turn red when the selected cell when the cell is the clicked
        if self.select:
            pygame.draw.rect(screen, CELL_SELECTED_COLOR, pygame.Rect(self.col * SQUARE_SIZE, self.row * SQUARE_SIZE,
                                                                SQUARE_SIZE, SQUARE_SIZE), 2)
            self.select = False

        # if-statements that will let us have the right value at the right location
        if self.value == 0:
            num_rect = num0_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
        if self.value == 1:
            num_rect = num1_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num1_surf, num_rect)
        if self.value == 2:
            num_rect = num2_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num2_surf, num_rect)
        if self.value == 3:
            num_rect = num3_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num3_surf, num_rect)
        if self.value == 4:
            num_rect = num4_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num4_surf, num_rect)
        if self.value == 5:
            num_rect = num5_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            # screen.blit places numbers inside the actual screen
            screen.blit(num5_surf, num_rect)
        if self.value == 6:
            num_rect = num6_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num6_surf, num_rect)
        if self.value == 7:
            num_rect = num7_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num7_surf, num_rect)
        if self.value == 8:
            num_rect = num8_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num8_surf, num_rect)
        if self.value == 9:
            num_rect = num9_surf.get_rect(
                center=(SQUARE_SIZE * self.col + SQUARE_SIZE // 2, SQUARE_SIZE * self.row + SQUARE_SIZE // 2))
            screen.blit(num9_surf, num_rect)

