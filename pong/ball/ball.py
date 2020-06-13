"""The Ball class handles then logic and rendering of the ball object
It is also responsible for updating the score of a paddle
if it collides with the opposing wall
"""
from os import getcwd
from os.path import join, abspath
import pygame
from utils.constants import (
    INITIAL_BALL_RAD,
    INITIAL_BALL_SPEED,
    INITIAL_BALL_POS,
    BOARD_WIDTH,
    BOARD_HEIGHT,
    BORDER_THICKNESS
)


class Ball:
    """Class for the ball object. Keeps track of size, speed, direction,
    and last hitter.
    """

    def __init__(self):
        """Initialises the ball at x, y (0, 0), speed of (0, 0), and a
        radius of INITIAL_BALL_RAD pixels
        Args:
            board (board): The palying board that the ball belongs to
        """

        self.coords = INITIAL_BALL_POS
        self.diameter = 2 * INITIAL_BALL_RAD
        self.speed = INITIAL_BALL_SPEED
        # V: 1 for down, -1 for up; H: 1 for right, -1 for left
        self.direction = {'V': 1, 'H': 1}
        self.color = (255, 0, 255)
        self.image = pygame.transform.scale(pygame.image.load(
                        join(abspath(getcwd()), 'pong', 'images', 'intro_ball.gif')).convert(),
                                            (self.diameter, self.diameter))

    def update(self):
        """Updates the position of the ball, and handles the logic for when
        the ball collides with the edges of the board

        Reverses the direction when the ball's exceeds or meets the borders
        or the bounds of the board either left or right, or up or down
        """
        old_coords = self.coords
        # Handle the horizontal movement of the ball
        if old_coords[0] + self.diameter >= BOARD_WIDTH or old_coords[0] <= 0:
            # Reverse the direction when we exceed or meet the bounds of the
            # board either left or right, or up or down
            self.direction['H'] = -(self.direction['H'])

        # Handle the vertical movement of the ball
        if (old_coords[1] + self.diameter >= BOARD_HEIGHT - BORDER_THICKNESS
                or old_coords[1] <= 0 + BORDER_THICKNESS):
            self.direction['V'] = -(self.direction['V'])

        new_coords = (old_coords[0] + self.direction['H'] *
                      self.speed[0],
                      old_coords[1] + self.direction['V'] *
                      self.speed[1])
        self.coords = new_coords

    def reverse_horizontal_direction(self):
        """Reverses the ball's horizontal direction
        """
        self.direction['H'] = -(self.direction['H'])

    def get_image(self):
        """Returns a pygame image object of the ball
        """
        return self.image

    def get_rect(self):
        """Returns a pygame Rect object at the current positon and
        size of the ball
        """
        ball_rect = pygame.Rect((self.coords), (self.diameter, self.diameter))
        return ball_rect
