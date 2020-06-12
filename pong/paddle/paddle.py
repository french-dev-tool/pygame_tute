"""Creates and handles the logic for the Paddle class
"""
import pygame
from utils.constants import BOARD_WIDTH


class Paddle:
    """Paddle for the player to hit the ball with.

    Initialises the paddle at [0, 0] width a set width and height,
    then returns the newly created object
    """

    def __init__(self, player, color):
        """Initialises the paddle at [0,0] with a starting width and height, and keeps
        track of the player's current score
        """
        self.width = 5
        self.height = 50
        if player == 1:
            self.coords = [0, 0]
        else:
            self.coords = [BOARD_WIDTH - self.width, 0]
        self.score = 0
        self.color = color

    def move_paddle(self, direction, distance):
        """Moves the paddle some distance in the vertical axis as long as the paddle is
        within the bounds of the board
        """
        # + direction is downward, - direction is upward
        if direction == 0:
            self.coords[1] = self.coords[1] + distance
        else:
            self.coords[1] = self.coords[1] - distance

    def get_rect(self):
        """Gets the paddle's current Rect.
        """
        paddle_rect = pygame.Rect(
            (self.coords[0], self.coords[1], self.width, self.height))
        return paddle_rect
