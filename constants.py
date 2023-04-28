# this will be a file that contains all the constants that our sudoku file can actually use to
# define the the dimensions of our boxes, lines, and to also give us the colors that we want to use throughout our
# sudoku game

# centralized color variables with tuple codes that any other variable can draw upon

RED = (255, 0, 0, 255)
BRICK = (156,102,31)
BLACK = (0, 0, 0, 255)
CORAL = (255,114,86)
GRAY =  (190, 190, 190, 255)
GOLD = (255, 215, 0, 255),
WHITE = (255, 255, 255, 255)
VIOLET = (238, 130, 238, 255)
FLORAL_WHITE = (255,250,240)
SALMON = (233,150,122)
GRAY33 = (84,84,84)

# dimensions of the board and cells

WIDTH = 900
HEIGHT = 1000
CELL_D = 100
BOX_D = 300
BOTTOM_B  = HEIGHT - CELL_D # bottom box
SQUARE_SIZE = (WIDTH/9)
# need to look through my class files,
# i dont remember using SQUARE_SIZE, perhaps I used it while following Professor Zhou tic tac toe example



# additional variables binding num boxes, cols, rows

BOARD_ROWS = 9
BOARD_SIZE = 9
BOARD_COLS = 9
SPACE = 55



# width of the cell (reg_width) and box lines (bold_lines)

LINE_WIDTH_BOLD = 7
LINE_WIDTH_CELL = 3
WIN_LINE_WIDTH = 15



# color of different objects in the game

BG_COLOR = BRICK
LINE_COLOR = BLACK
CELL_NOT_SELECTED = BLACK
CELL_SELECTED = RED
NUM_COLOR = GOLD
BUTTON_TEXT_COLOR = CORAL
COLOR_SKETCH = GRAY
BUTTON_COLOR = GRAY33

# size of font for different text surfaces

WELCOME_SIZE = 80
DIFF_SIZE = 60
NUM_SIZE = 60
GAME_WIN_FONT = 70
GAME_LOSS_FONT = 70
BUTTON_TEXT_SIZE = 40


# pygame SysFont

WELCOME_FONT = 'corbel'
GAME_DIFF_FONT = WELCOME_FONT
BUTTON_FONT = 'ebrima'
NUM_FONT = 'dubai'


