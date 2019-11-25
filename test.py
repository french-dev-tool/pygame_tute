import sys
import pygame
from pygame import *

pygame.init()

size = width, height = 700, 450
speed = 1
# Start at middle of the screen and extend in 
middle = width / 2, height / 2
head = Rect(middle[0], middle[1], 5, 5)

print(head)

screen = pygame.display.set_mode(size)

background = pygame.Surface(screen.get_size()).convert()
background.fill((250, 250, 250))

screen.blit(background, (0, 0))
pygame.display.flip()

while 1:
    for event in pygame.event.get():
        if event.type == QUIT:
            sys.exit()

    head.left = head.left - speed
    head.right = head.right - speed
    screen.blit(background, head)
    pygame.display.flip()

