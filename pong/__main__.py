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

def start_the_game():
    """Starts the game
    """
    print('Hi')

def set_difficulty(value, difficulty):
    """Sets the difficulty
    """
    print(value, difficulty)

def draw_menu(screen):
    """Draws the menu images and title
    """
    pass

def menu(screen):
    """Displays the main menu to the user
    """
    draw_menu(screen)

    # Wait in the menu until the user presses enter/q
    while True:
        for event in pygame.event.get():
            if event.type is QUIT:
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
            if event.type is pygame.KEYDOWN:
                key = event.key
                if key is pygame.locals.K_q:
                    pygame.quit()
                elif (key is pygame.locals.K_RETURN
                      or key is pygame.locals.K_ESCAPE
                      or key is pygame.locals.K_p):
                    return False

def setup():
    """Sets up the game for playing and initialises objects
    """
    clock = pygame.time.Clock()
    display = pygame.display
    screen = display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

    player = Paddle(player_color)
    ball_one = Ball((4, 3))
    ball_two = Ball((3, 2))
    pygame.display.flip()
    board = Board(screen=screen,
                  player=player,
                  balls=[ball_one, ball_two])
    return board, clock, display

def main():
    """Handles logic associated with playing the game
    """
    board, clock, display = setup()
    running, show_menu = True, True
    pause_count = 0

    while running:
        if show_menu:
            show_menu = menu(screen)
            if pause_count == 0:
                pygame.time.delay(1500)
                pause_count = pause_count + 1

        board.draw()
        display.set_caption(f'Current Score: {board.player.score}')
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == QUIT:
                # pylint: disable=no-member
                pygame.quit()
                # pylint: enable=no-member
            elif event.type == KEYDOWN:
                key = event.key
                if key is pygame.locals.K_ESCAPE or key is pygame.locals.K_p:
                    show_menu = True
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
        if board.lost():
            # End the game if the ball hits the left wall
            print(f'Congratulations, your score was {board.player.score}!')
            running = False


if __name__ == '__main__':
    # pylint: disable=no-member
    pygame.init()
    # pylint: enable=no-member
    main()
