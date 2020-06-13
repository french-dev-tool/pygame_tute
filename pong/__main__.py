"""Main class of the pong game.
Handles all logic associated with playing the game solo or with an opponent
"""
import os
import pygame
import pygame.locals
from pygame.constants import QUIT, KEYDOWN, KEYUP
from math import floor

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


def set_difficulty(difficulty):
    """Sets the difficulty
    """

    return difficulty


def setup():
    """Sets up the game for playing and initialises objects
    """

    pygame.init()

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


def draw_menu(display):
    """Draws the menu options, instruction_one, and title
    """

    img_dir = os.path.join(os.curdir, 'pong', 'images')
    screen = display.get_surface()
    background = pygame.Surface(screen.get_size()).convert()

    font_color = pygame.Color("black")
    title_font = pygame.font.Font(None, 48)
    text_font = pygame.font.Font(None, 24)

    title = title_font.render("Squash", 1, font_color)
    title_pos = title.get_rect()
    title_pos.centerx = background.get_rect().centerx
    title_pos.centery = 30

    instructions_start_y = floor(background.get_size()[1] / 5)
    seperation = 50

    # TODO move these to an image, or few images
    instruction_one = text_font.render("To play, press [ENTER], [ESC], or P",
                                       1, font_color)
    instruction_one_pos = instruction_one.get_rect()
    instruction_one_pos.centerx = background.get_rect().centerx
    instruction_one_pos.centery = instructions_start_y

    instruction_two = text_font.render("To pause, press [ESC] or P", 1,
                                       font_color)
    instruction_two_pos = instruction_two.get_rect()
    instruction_two_pos.centerx = background.get_rect().centerx
    instruction_two_pos.centery = instructions_start_y + seperation

    instruction_three = text_font.render("To quit, press Q whilst paused",
                                         1, font_color)
    instruction_three_pos = instruction_three.get_rect()
    instruction_three_pos.centerx = background.get_rect().centerx
    instruction_three_pos.centery = instruction_two_pos.centery + seperation

    instruction_four = text_font.render("Use W and S to move. Don't let the ball hit the wall!",
                                        1, font_color)
    instruction_four_pos = instruction_four.get_rect()
    instruction_four_pos.centerx = background.get_rect().centerx
    instruction_four_pos.centery = instruction_three_pos.centery + seperation

    # Load a background image
    bg_image = pygame.image.load(os.path.join(
        img_dir, 'bg_image.jpg')).convert()
    bg_image = pygame.transform.scale(bg_image, screen.get_size())
    bg_image_rect = bg_image.get_rect()
    background.blit(bg_image, bg_image_rect)

    background.blit(title, title_pos)
    background.blit(instruction_one, instruction_one_pos)
    background.blit(instruction_two, instruction_two_pos)
    background.blit(instruction_three, instruction_three_pos)
    background.blit(instruction_four, instruction_four_pos)

    screen.blit(background, (0, 0))

    pygame.display.flip()


def menu(display):
    """Draws the main menu and handles the exit state from the menu
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
    show_menu = False
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
        print(f'Congratulations, your final score was {board.player.score}!')
        show_menu = True
    return show_menu


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
        show_menu = game_loop(board)
    pygame.quit()

if __name__ == '__main__':
    main()
