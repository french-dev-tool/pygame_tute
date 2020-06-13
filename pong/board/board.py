"""Board class of the pong game
"""
import pygame
from utils.constants import BOARD_WIDTH, BOARD_HEIGHT, BORDER_THICKNESS
from border.border import Border

border_color = pygame.Color("yellow")
border_b_origin = (0, BOARD_HEIGHT - BORDER_THICKNESS)
border_r_origin = (BOARD_WIDTH - BORDER_THICKNESS, 0 + BORDER_THICKNESS)

class Board:
    """Board for the player or players to play on as a surface"""

    def __init__(self, screen, player, balls):
        """Initialise the board with height and width specified in utils.constants"""
        self.screen = screen
        self.height = screen.get_height()
        self.width = screen.get_width()
        self.borders = {
            Border('t'): pygame.Rect((0, 0),
                                     (BOARD_WIDTH, BORDER_THICKNESS)),
            Border('b'): pygame.Rect(border_b_origin,
                                     (BOARD_WIDTH, BORDER_THICKNESS)),
            Border('r'): pygame.Rect(border_r_origin,
                                     (BORDER_THICKNESS,
                                      BOARD_HEIGHT - BORDER_THICKNESS))
        }
        self.player = player
        self.balls = balls


    def determine_paddle_collision(self, ball):
        """Returns true if the ball collides with the paddle
        """
        return ball.get_rect().colliderect(self.player.get_rect())


    def determine_border_collision(self, ball, border):
        """Returns true if the ball collides with specified border
        """
        return ball.get_rect().colliderect(self.borders[border])


    def lost(self):
        """Returns true if the game is lost, that is if any balls touch the left wall
        """
        for ball in self.balls:
            if ball.coords[0] < 0:
                return True
        return False


    def draw(self):
        """Draw the board, with paddles and ball
        """
        self.screen.fill(pygame.Color("black"))
        player_rect = self.player.get_rect()

        for ball in self.balls:
            ball.update()
            ball_rect = ball.get_rect()

            if self.determine_paddle_collision(ball):
                ball.reverse_horizontal_direction()
                ball.increase_speed()
                self.player.increment_score()

            if self.determine_border_collision(ball, Border('r')):
                ball.reverse_horizontal_direction()

            if (self.determine_border_collision(ball, Border('t'))
                    or self.determine_border_collision(ball, Border('b'))):
                ball.reverse_vertical_direction()
            pygame.draw.rect(self.screen, ball.color, ball_rect)
            self.screen.blit(ball.get_image(), ball_rect)

        pygame.draw.rect(self.screen, self.player.color, player_rect)
        pygame.draw.rect(self.screen, pygame.Color("yellow"), self.borders[Border('t')])
        pygame.draw.rect(self.screen, pygame.Color("yellow"), self.borders[Border('b')])
        pygame.draw.rect(self.screen, pygame.Color("yellow"), self.borders[Border('r')])

        pygame.display.flip()
