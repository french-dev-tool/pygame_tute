"""Creates and handles the logic for the Paddle class
"""
import pygame
from utils.constants import BOARD_HEIGHT, BORDER_THICKNESS

class Paddle:
    """Paddle for the player to hit the ball with.

    Initialises the paddle at (0, 0), with a set width and height,
    then returns the newly created object
    """

    def __init__(self, color):
        """Initialises the paddle at (0,0) with a starting width and height,
        and keeps track of the player's current score
        """
        self.width = 5
        self.height = 50
        self.speed = 15
        self.coords = (0, BORDER_THICKNESS)
        self.score = 0
        self.color = color


    def increment_score(self):
        """Increments the player's score by one
        """
        self.score = self.score + 1
        

    def move_paddle(self, direction):
        """Moves the paddle some distance in the vertical axis as long as
        the paddle is within the bounds of the board
        """
        old_coords = self.coords
        # Update the position of the paddle when new pos is valid
        new_coords = (0, old_coords[1] + direction * self.speed)
        # If new coords is less than border thickness, set y to B_T
        if new_coords[1] <= 0 + BORDER_THICKNESS:   
            new_coords = (0, BORDER_THICKNESS)
        # elif new coords > HEIGHT - B_T set y to h - B_T
        elif new_coords[1] + self.height >= BOARD_HEIGHT - BORDER_THICKNESS:
            new_coords = (0, BOARD_HEIGHT - BORDER_THICKNESS - self.height)
        # Set self.coords to new_coords in each situation
        self.coords = new_coords


    def get_rect(self):
        """Gets the paddle's current Rect.
        """
        paddle_rect = pygame.Rect(
            (self.coords[0], self.coords[1], self.width, self.height))
        return paddle_rect
