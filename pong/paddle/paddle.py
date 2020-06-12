"""Creates and handles the logic for the Paddle class
"""


class Paddle:
    """Paddle for the player to hit the ball with.

    Initialises the paddle at [0, 0] width a set width and height,
    then returns the newly created object
    """

    def __init__(self):
        """Initialises the paddle at [0,0] with a starting width and height, and keeps
        track of the player's current score
        """
        self.width = 5
        self.height = 50
        self.coords = [0, 0]
        self.score = 0

    def move_paddle(self, distance):
        """Moves the paddle some distance in the vertical axis as long as the paddle is
        within the bounds of the board
        """
        self.coords[1] = self.coords[1] + distance

    def update_position(self):
        """Updates the position of the ball.
        """
        pass

    def show(self):
        """Shows the paddle's current position.
        """
        pass
