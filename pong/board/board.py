"""Board class of the pong game
"""


class Board:
    """Board for the player or players to play on as a surface"""

    def __init__(self, height, width, border_width, player_one, player_two, ball):
        """Initialise the board with height and width specified in utils.constants"""
        self.height = height
        self.width = width
        self.border_width = border_width
        self.player_one = player_one
        self.player_two = player_two
        if player_two is None:
            self.player_count = 1
        else:
            self.player_count = 2
        self.ball = ball

    def move_paddle(self, paddle, distance):
        """Moves the paddle some distance in the vertical axis as long as the paddle is
        within the bounds of the board
        """
        if paddle.coords[1] + distance < 0 or paddle.coords[1] + paddle.height + distance > self.height:
            return
        paddle.coords[1] = paddle.coords[1] + distance

    def update_score(self, ball_collided_with):
        """Update the score of the paddle that opposes the side of the board
        that the ball collides with
        """
        if ball_collided_with == 'left_wall':
            # update right paddle
            self.player_two.score = self.player_two.score + 1

        else:
            # update left paddle
            self.player_one.score = self.player_one.score + 1

            pass
        pass
