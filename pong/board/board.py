"""Board class of the pong game
"""


class Board:
    """Board for the player or players to play on as a surface"""

    def __init__(self, height, width, border_width):
        """Initialise the board with height and width specified in utils.constants"""
        self.height = height
        self.width = width
        self.border_width = border_width
