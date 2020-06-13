"""Main class of the pong game.
Handles all logic associated with playing the game solo or with an opponent
"""
import math
import pygame
import pygame.locals
# from pygame import locals as pygame_locals
# pylint: disable=no-name-in-module
from pygame.constants import QUIT, KEYDOWN, KEYUP
# pylint: enable=no-name-in-module

from utils.constants import (
    BOARD_HEIGHT,
    BOARD_WIDTH,
    BOARD_EDGE_MULTIPLIER,
    BORDER_THICKNESS,
    FPS
)
from paddle.paddle import Paddle
from board.board import Board
from ball.ball import Ball

border_color = pygame.Color("yellow")
player_color = pygame.Color("red")
player_two_color = pygame.Color("blue")


def setup():
    """Sets up the game for playing and initialises objects
    """
    print('Initialising...')
    # Setup pygame before creating all of our objects
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member
    clock = pygame.time.Clock()

    screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))   
    player = Paddle(player_color)
    ball = Ball()

    pygame.display.flip()
    board = Board(screen=screen,
                  player=player,
                  ball=ball)
    board.draw()
    return board, clock


def main():
    """Handles all logic associated with playing the game solo or with an opponent
    """
    board, clock = setup()
    # Main loop
    while True:
        ms_elapsed = clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
            elif event.type == KEYDOWN:
                key = event.key
                if key is pygame.locals.K_s:
                    board.player.move_paddle(1)
                if key is pygame.locals.K_w:
                    board.player.move_paddle(-1)
            elif event.type == KEYUP:
                key = event.key
                if key is pygame.locals.K_s:
                    board.player.move_paddle(1)
                if key is pygame.locals.K_w:
                    board.player.move_paddle(-1)
        board.draw()


if __name__ == '__main__':
    pygame.init()
    main()
