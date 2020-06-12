"""The Ball class handles then logic and rendering of the ball object
It is also responsible for updating the score of a paddle
if it collides with the opposing wall
"""
from os import getcwd
from os.path import join, abspath
import pygame
from utils.constants import (
    INITIAL_BALL_RAD, INITIAL_BALL_SPEED, INITIAL_BALL_POS, BOARD_WIDTH
)


class Ball:
    """Class for the ball object. Keeps track of size, speed, direction,
    and last hitter.
    """

    def __init__(self):
        """Initialises the ball at x, y (0, 0), speed of (0, 0), and a
        radius of INITIAL_BALL_RAD pixels
        """
        self.coords = INITIAL_BALL_POS
        self.diameter = 2 * INITIAL_BALL_RAD
        self.speed = INITIAL_BALL_SPEED
        self.color = (255, 0, 255)
        self.image = pygame.transform.scale(pygame.image.load(
            join(abspath(getcwd()), 'pong', 'images', 'intro_ball.gif')).convert(), (self.diameter, self.diameter))

    def update(self):
        """Updates the position of the ball.
        """
        old_coords = self.coords
        # Moving in the left-right direction its within the bounds of the board
        if old_coords[0] + self.diameter <= BOARD_WIDTH and old_coords[0] >= 0:
            new_coords = (old_coords[0] + self.speed[0], old_coords[1])
        else:
            new_coords = self.coords
        self.coords = new_coords

    def get_image(self):
        """Returns the ball image
        """
        return self.image

    def get_rect(self):
        """Shows the ball's current position.
        """
        ball_rect = pygame.Rect((self.coords), (self.diameter, self.diameter))
        return ball_rect
