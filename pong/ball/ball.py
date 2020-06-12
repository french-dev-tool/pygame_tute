"""The Ball class handles then logic and rendering of the ball object
It is also responsible for updating the score of a paddle
if it collides with the opposing wall
"""
from utils.constants import INITIAL_BALL_RAD, INITIAL_BALL_SPEED


class Ball:
    """Class for the ball object. Keeps track of size, speed, direction, 
    and last hitter.
    """

    def __init__(self):
        """Initialises the ball at x, y [0, 0], speed of [0, 0], and a 
        radius of INITIAL_BALL_RAD pixels
        """
        self.coords = [0, 0]
        self.radius = INITIAL_BALL_RAD
        self.speed = INITIAL_BALL_SPEED
        self.color = (255, 0, 255)

    def update_position():
        """Updates the position of the ball.
        """
        pass

    def show():
        """Shows the ball's current position.
        """
        pass
