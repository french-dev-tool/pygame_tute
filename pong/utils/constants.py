"""Stores the required constants that are used in initialising the game
"""
from math import floor


BOARD_HEIGHT = 480
BOARD_WIDTH = 720
BOARD_EDGE_MULTIPLIER = 0.02 # Give 2% of screen size as edge
BORDER_THICKNESS = floor(BOARD_EDGE_MULTIPLIER * BOARD_HEIGHT)
INITIAL_BALL_RAD = 10
INITIAL_BALL_POS = (floor(0.1 * BOARD_WIDTH) - floor(INITIAL_BALL_RAD / 2),
                    floor(BOARD_HEIGHT / 2) - floor(INITIAL_BALL_RAD / 2))
FPS = 30
