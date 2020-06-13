"""Main class of the pong game.
Handles all logic associated with playing the game solo or with an opponent
"""
import pygame
import pygame.locals
# from pygame import locals as pygame_locals
# pylint: disable=no-name-in-module
from pygame.constants import QUIT, KEYDOWN, KEYUP
# pylint: enable=no-name-in-module

from utils.constants import (
    BOARD_HEIGHT,
    BOARD_WIDTH,
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
    display = pygame.display
    screen = display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))
    player = Paddle(player_color)
    ball = Ball()
    pygame.display.flip()
    board = Board(screen=screen,
                  player=player,
                  ball=ball)
    board.draw()
    return board, clock, display


def main():
    """Handles logic associated with playing the game solo
    """
    board, clock, display = setup()
    quit_game = False
    # Main loop
    while True:
        display.set_caption(f'Current Score: {board.player.score}')
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT or quit_game:
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
        if board.ball.coords[0] < 0:
            # End the game if the ball hits the left wall
            print(f'Congratulations, Your score was {board.player.score}!')
            quit_game = True
        board.draw()


if __name__ == '__main__':
    pygame.init()
    main()
