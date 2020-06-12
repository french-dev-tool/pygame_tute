"""Main class of the pong game.
Handles all logic associated with playing the game solo or with an opponent
"""
import math
import pygame
# pylint: disable=no-name-in-module
from pygame.constants import QUIT, KEYDOWN
# pylint: enable=no-name-in-module

from utils.constants import BOARD_HEIGHT, BOARD_WIDTH, BOARD_EDGE_MULTIPLIER
from paddle.paddle import Paddle
from board.board import Board
from ball.ball import Ball

border_width = math.floor(BOARD_EDGE_MULTIPLIER * BOARD_HEIGHT)


def main():
    """Handles all logic associated with playing the game solo or with an opponent
    """
    # Setup pygame before creating all of our objects
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member
    screen = pygame.display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    pygame.draw.rect(screen, pygame.Color("white"),
                     pygame.Rect((0, 0, border_width, BOARD_HEIGHT)))
    pygame.display.flip()

    player_one = Paddle()
    player_two = Paddle()
    ball = Ball()
    board = Board(BOARD_HEIGHT, BOARD_WIDTH,
                  BOARD_WIDTH * BOARD_EDGE_MULTIPLIER, player_one, player_two, ball)

    print(player_one, board, ball)
    # print(board.player_count)

    while True:
        for event in pygame.event.get():
            print(event.type)
            if event.type == QUIT:
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
            if event.type == KEYDOWN:
                print(event.type)


if __name__ == '__main__':
    main()
