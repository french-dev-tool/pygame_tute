from utils.constants import INITIAL_BALL_RAD, INITIAL_BALL_SPEED


class Ball:
    """Class for the ball object. Keeps track of size, speed, direction, and last hitter."""

    def __init__(self):
        """Initialises the ball at x, y [0, 0], speed of [0, 0], and a radius
        of INITIAL_BALL_RAD pixels
        """
        self.coords = [0, 0]
        self.radius = INITIAL_BALL_RAD
        self.speed = INITIAL_BALL_SPEED
