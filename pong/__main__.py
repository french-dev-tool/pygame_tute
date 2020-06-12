"""Main class of the pong game.
Handles all logic associated with playing the game solo or with an opponent
"""
import math
import pygame
import pygame.locals
# from pygame import locals as pygame_locals
# pylint: disable=no-name-in-module
from pygame.constants import QUIT, KEYDOWN
# pylint: enable=no-name-in-module

from utils.constants import BOARD_HEIGHT, BOARD_WIDTH, BOARD_EDGE_MULTIPLIER, FPS
from paddle.paddle import Paddle
from board.board import Board
from ball.ball import Ball

border_width = math.floor(BOARD_EDGE_MULTIPLIER * BOARD_HEIGHT)
border_color = pygame.Color("yellow")
player_one_color = pygame.Color("red")
player_two_color = pygame.Color("blue")


def main():
    """Handles all logic associated with playing the game solo or with an opponent
    """
    print('Initialising...')
    # Setup pygame before creating all of our objects
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    border_t = pygame.draw.rect(screen, border_color,
                                pygame.Rect((0, 0, BOARD_WIDTH, border_width)))

    border_b_top_left = BOARD_HEIGHT - border_width
    border_b = pygame.draw.rect(screen, border_color,
                                pygame.Rect((0, border_b_top_left,
                                             BOARD_WIDTH, border_width)))

    pygame.display.flip()

    player_one = Paddle(1, player_one_color)
    player_two = Paddle(2, player_two_color)
    ball = Ball()
    board = Board(screen,
                  BOARD_HEIGHT,
                  BOARD_WIDTH,
                  border_t,
                  border_b,
                  player_one,
                  player_two,
                  ball)

    print(player_one, board, ball)
    board.draw()

    # Main game loop
    while True:
        ms_elapsed = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
            if event.type == KEYDOWN:
                key = event.key
                if key is pygame.locals.K_w:
                    player_one.move_paddle(0, 15)
                if key is pygame.locals.K_s:
                    player_one.move_paddle(1, 15)
        board.draw()


if __name__ == '__main__':
    pygame.init()
    main()
