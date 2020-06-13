"""Main class of the pong game.
Handles all logic associated with playing the game solo or with an opponent
"""
import os
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
DIFFICULTY = 0.1

def set_difficulty(value, difficulty):
    """Sets the difficulty
    """
    print(value, difficulty)

def setup():
    """Sets up the game for playing and initialises objects
    """
    clock = pygame.time.Clock()
    display = pygame.display
    screen = display.set_mode((BOARD_WIDTH, BOARD_HEIGHT))

    player = Paddle(player_color)
    ball_one = Ball((4, 3), DIFFICULTY)
    ball_two = Ball((3, 2), DIFFICULTY)
    board = Board(screen=screen,
                  player=player,
                  balls=[ball_one, ball_two])
    return board, clock, display

# TODO implement this method properly
def draw_menu(display):
    """Draws the menu images and title
    """
    surface = display.get_surface()
    img_dir = os.path.join(os.curdir, 'pong', 'images')
    # Load an image
    black_square = pygame.image.load(os.path.join(
        img_dir, 'black_square_6.jpg')).convert()
    black_square = pygame.transform.scale(surface, (BOARD_WIDTH, BOARD_HEIGHT))

    # Get images rect
    black_square_rect = black_square.get_rect()
    # Blit image onto rect
    surface.blit(black_square, black_square_rect)

    pygame.display.update()

def menu(display):
    """Displays the main menu to the user
    """
    draw_menu(display)

    # Wait in the menu until the user presses enter/q
    while True:
        for event in pygame.event.get():
            if event.type is QUIT:
                pygame.quit()
            if event.type is pygame.KEYDOWN:
                key = event.key
                if key is pygame.locals.K_q:
                    pygame.quit()
                elif (key is pygame.locals.K_RETURN
                      or key is pygame.locals.K_ESCAPE
                      or key is pygame.locals.K_p):
                    return False

def game_loop(board):
    """Handles the main game loop
    """
    show_menu, running = False, True
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
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
    return show_menu, running

def main():
    """Handles logic associated with playing the game
    """
    board, clock, display = setup()
    running, show_menu = True, True
    pause_count = 0

    while running:
        if show_menu:
            show_menu = menu(display)
            if pause_count == 0:
                pygame.time.delay(1500)
                pause_count = pause_count + 1

        board.draw()
        display.set_caption(f'Current Score: {board.player.score}')
        clock.tick(FPS)
        show_menu, running = game_loop(board)

if __name__ == '__main__':
    pygame.init()
    main()
