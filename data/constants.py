WINDOW_CAPTIONS = 'Pathfinding Visualizations'

CANVAS_HEIGHT = 899
CANVAS_WIDTH = 899

SCREEN_PADDING = 5

MENU_HEIGHT = 100
MENU_WIDTH = CANVAS_WIDTH
MENU_PADDING = 5  # the padding between the menu and canvas

SCREEN_HEIGHT = CANVAS_HEIGHT + MENU_HEIGHT + 2*SCREEN_PADDING + MENU_PADDING
SCREEN_WIDTH = CANVAS_WIDTH + 2*SCREEN_PADDING

NODE_PADDING = 1
MENU_CENTER = (int(SCREEN_WIDTH/2), int(MENU_HEIGHT/2 + SCREEN_PADDING))
CANVAS_CENTER = (int(SCREEN_WIDTH/2), int(SCREEN_HEIGHT-SCREEN_PADDING-CANVAS_HEIGHT/2))
CANVAS_START_Y = SCREEN_PADDING + MENU_PADDING + MENU_HEIGHT
CANVAS_START_X = SCREEN_PADDING

# colors
BG_COLOR = (24, 32, 38)
MENU_COLOR = (124, 160, 192)  # https://www.color-hex.com/color/7ca0c0
CANVAS_COLOR = (176, 197, 217)


WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
DARK_GREY_BLUE = (47, 54, 59)
BRIGHT_LIGHT_GREEN = (122, 255, 122)


# canvas-related
DEFAULT_ROWS = 50
DEFAULT_COLS = DEFAULT_ROWS
START_IMAGE = 'start.png'
GOAL_IMAGE = 'goal.png'

# Node states
N_BLANK = 1
N_BLOCKED = 2
N_GOAL = 3
N_START = 4
N_OPEN_SET = 5
N_CLOSED_SET = 6
N_PATH = 7

COLOR_BLANK = WHITE
COLOR_BLOCKED = DARK_GREY_BLUE
COLOR_OPEN = (102, 204, 204)
COLOR_CLOSED = (178, 229, 229)
COLOR_PATH = BRIGHT_LIGHT_GREEN
COLOR_START = (0, 0, 255)
COLOR_GOAL = (255, 0, 0)

NODE_COLORS = {N_BLANK: COLOR_BLANK,
               N_BLOCKED: COLOR_BLOCKED,
               N_OPEN_SET: COLOR_OPEN,
               N_CLOSED_SET: COLOR_CLOSED,
               N_PATH: COLOR_PATH,
               N_START: COLOR_START,
               N_GOAL: COLOR_GOAL}

# mouse-related
# different cursor settings
M_CLEAR = 1
M_BLOCK = 2
M_START = 3
M_GOAL = 4
M_INC_WEIGHT = 5
M_DEC_WEIGHT = 6

# cursor colors
CURSOR_COLOR = {M_CLEAR: COLOR_BLANK,
                M_BLOCK: COLOR_BLOCKED,
                M_START: COLOR_START,
                M_GOAL: COLOR_GOAL,
                M_INC_WEIGHT: DARK_GREY_BLUE,
                M_DEC_WEIGHT: (230, 230, 230)}

# maybe add separate mouse colors
# M_COLOR_CLEAR: COLOR_BLANK,
# M_COLOR_BLOCK: COLOR_BLOCKED,
# M_COLOR_START: COLOR_START,
# M_COLOR_GOAL: COLOR_GOAL

# App settings
A_ROWS = 1
A_COLS = 2
A_ALGORITHM = 3

"""
Classes:
  Node
    attr:

  Board -> rename Graph

  -----

  App -> has the main loop
    attr:
    settings -> dict
  AppElement
  Menu(AppElement)
  Grid(AppElement)
  Mouse

  -----

  Algorithm
    Disjkstras
    BreadthFirst
    DepthFirst
    AStar
"""
