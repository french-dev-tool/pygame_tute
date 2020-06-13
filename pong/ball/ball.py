"""The Ball class handles then logic and rendering of the ball object
It is also responsible for updating the score of a paddle
if it collides with the opposing wall
"""
from os import getcwd
from os.path import join, abspath
from math import floor
import pygame
from utils.constants import (
    INITIAL_BALL_RAD,
    INITIAL_BALL_POS
)


class Ball:
    """Class for the ball object. Keeps track of size, speed, direction,
    and last hitter.
    """

    def __init__(self, speed, difficulty):
        """Initialises the ball with a speed and a
        radius of INITIAL_BALL_RAD pixels

        Args:
            Speed (speed): A tuple containing integer values for (x_speed, y_speed)
        """

        self.coords = INITIAL_BALL_POS
        self.diameter = 2 * INITIAL_BALL_RAD
        self.speed = speed # Tuple, (x, y) of speed
        # TODO implement speed modifier changes based on difficulty/pickups
        self.speed_modifier = difficulty
        # V: 1 for down, -1 for up; H: 1 for right, -1 for left
        self.direction = {'V': 1, 'H': 1}
        self.color = (255, 0, 255)
        self.image = pygame.transform.scale(pygame.image.load(
                        join(abspath(getcwd()), 'pong', 'images', 'intro_ball.gif')).convert(),
                                            (self.diameter, self.diameter))

    def update(self):
        """Updates the position of the ball as a function of the balls current speed
        """
        old_coords = self.coords
        new_coords = (old_coords[0] + self.direction['H'] * self.speed[0],
                      old_coords[1] + self.direction['V'] * self.speed[1])
        self.coords = new_coords

    def increase_speed(self):
        """Increases the ball's speed
        """
        new_speed = (self.speed[0] + floor(self.speed_modifier * self.speed[1]), self.speed[1])
        self.speed = new_speed

    def reverse_horizontal_direction(self):
        """Reverses the ball's horizontal direction
        """
        self.direction['H'] = -(self.direction['H'])

    def reverse_vertical_direction(self):
        """Reverses the ball's vertical direction
        """
        self.direction['V'] = -(self.direction['V'])

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
