"""Board class of the pong game
"""
import pygame


class Board:
    """Board for the player or players to play on as a surface"""

    def __init__(self, screen, height, width, border_t, border_b, player_one, player_two, ball):
        """Initialise the board with height and width specified in utils.constants"""
        self.screen = screen
        self.height = height
        self.width = width
        self.border_t = border_t
        self.border_b = border_b
        self.player_one = player_one
        self.player_two = player_two
        if player_two is None:
            self.player_count = 1
        else:
            self.player_count = 2
        self.ball = ball

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

    def draw(self):
        """Draw the board, with paddles and ball
        """
        bg_color = pygame.Color("black")

        self.screen.fill(bg_color)

        player_one_rect = self.player_one.get_rect()

        self.ball.update()
        ball_rect = self.ball.get_rect()

        pygame.draw.rect(self.screen, self.player_one.color, player_one_rect)
        pygame.draw.rect(self.screen, pygame.Color("yellow"), self.border_t)
        pygame.draw.rect(self.screen, pygame.Color("yellow"), self.border_b)

        pygame.draw.rect(self.screen, self.ball.color, ball_rect)
        # Blit the ball image on the ball rect
        self.screen.blit(self.ball.get_image(), ball_rect)

        pygame.display.flip()
