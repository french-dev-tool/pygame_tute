"""Main class of the pong game.
Handles all logic associated with playing the game solo or with an opponent
"""
import pygame
# pylint: disable=no-name-in-module
from pygame.constants import MOUSEBUTTONDOWN, QUIT, MOUSEMOTION, KEYDOWN
# pylint: enable=no-name-in-module
from utils.constants import BOARD_HEIGHT, BOARD_WIDTH
from paddle.paddle import Paddle
from board.board import Board
from ball.ball import Ball


def main():
    """Handles all logic associated with playing the game solo or with an opponent
    """
    # Setup pygame before creating all of our objects
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member

    board = Board(BOARD_HEIGHT, BOARD_WIDTH, BOARD_WIDTH * 0.02)
    player_one = Paddle(board)
    ball = Ball()

    print(player_one, board, ball)

    for event in pygame.event.get():
        if event.type == QUIT:
            # pylint: disable=no-member
            pygame.quit()
            # pylint: enable=no-member
        # if event.type == KEYDOWN:


if __name__ == '__main__':
    main()
