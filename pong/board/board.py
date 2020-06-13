"""Board class of the pong game
"""
import pygame
from utils.constants import BOARD_WIDTH, BOARD_HEIGHT, BORDER_THICKNESS

border_color = pygame.Color("yellow")
border_b_origin = (0, BOARD_HEIGHT - BORDER_THICKNESS)
border_r_origin = (BOARD_WIDTH - BORDER_THICKNESS, 0 + BORDER_THICKNESS)

class Board:
    """Board for the player or players to play on as a surface"""

    def __init__(self, screen, player, ball):
        """Initialise the board with height and width specified in utils.constants"""
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.borders = {
            't': pygame.draw.rect(self.screen, border_color,
                                  pygame.Rect((0, 0),
                                              (BOARD_WIDTH, BORDER_THICKNESS))),
            'b': pygame.draw.rect(self.screen, border_color,
                                  pygame.Rect(border_b_origin,
                                              (BOARD_WIDTH, BORDER_THICKNESS))),
            'r': pygame.draw.rect(self.screen, border_color,
                                  pygame.Rect(border_r_origin,
                                              (BOARD_HEIGHT - BORDER_THICKNESS,
                                               BORDER_THICKNESS)))
        }
        self.player = player
        self.ball = ball

    def determine_collision(self):
        """Returns true if the ball collides with the paddle
        """
        return self.player.get_rect().colliderect(self.ball.get_rect())

    def draw(self):
        """Draw the board, with paddles and ball
        """
        bg_color = pygame.Color("black")
        self.screen.fill(bg_color)

        player_rect = self.player.get_rect()

        self.ball.update()
        ball_rect = self.ball.get_rect()
       
        if self.determine_collision():
            self.ball.reverse_horizontal_direction()
            self.player.increment_score()

        pygame.draw.rect(self.screen, self.player.color, player_rect)
        pygame.draw.rect(self.screen, pygame.Color("yellow"), self.borders['t'])
        pygame.draw.rect(self.screen, pygame.Color("yellow"), self.borders['b'])
        pygame.draw.rect(self.screen, pygame.Color("yellow"), self.borders['r'])

        pygame.draw.rect(self.screen, self.ball.color, ball_rect)
        self.screen.blit(self.ball.get_image(), ball_rect)

        pygame.display.flip()
