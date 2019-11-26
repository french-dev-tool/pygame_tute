import sys
from time import sleep
import pygame
from pygame import *


pygame.init()

size = width, height = 720, 640
speed = x_speed, y_speed = width // 15, height // 15

# Start at middle of the screen and extend in 
middle = 10, 20 # width / 2, height / 2
head = pygame.Surface([25, 25])
color = (255, 0, 0)
head.fill(color)

head_rect = head.get_rect()
head_rect.left, head_rect.top = 10, 10

screen = pygame.display.set_mode(size)

background = pygame.Surface(screen.get_size()).convert()
background.fill((255, 255, 255))

screen.blit(background, (0, 0))
pygame.display.flip()

pygame.draw.rect(background, (0, 0, 0), head_rect)
pygame.display.flip()

while 1:
    print(pygame.event.peek())
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    old_head_rect = head_rect
    # Blit over the old loc with a rect of equal size in the same color as BG
    # Else we retain a tail onto the background of the rect as it moves
    
    # Get the x, y of the old rect as a surface of same color as BG and blit it over 
    # screen.blit()
    new_pos = (head_rect.left + x_speed, head_rect.top)
    
    print(f'blitting head_rect at ({head_rect.left}, {head_rect.top})')
    head_rect.move(new_pos) 
    screen.blit(background, head_rect)
    pygame.display.flip()
    sleep(.5)

