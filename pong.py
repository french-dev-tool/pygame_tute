import pygame, sys
from pygame.locals import *

pygame.init()

size =  width, height = 480, 640
speed = [1,1]
position = posX, posY = 0, 0
white = 255,255,255
PADDLE_H = 200
PADDLE_W = 20

paddle1 = pygame.Rect((2,2), (PADDLE_W, PADDLE_H))

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

screen = pygame.display.set_mode(size)
player1 = pygame.Surface((PADDLE_W, PADDLE_H))
player1.fill((200,200,200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

    pressed = pygame.key.get_pressed()
    if pressed[pygame.K_w]:
        if paddle1.top > 0:
            paddle1 = paddle1.move(0,-1)
    if pressed[pygame.K_s]:
        if paddle1.bottom < height:
            paddle1 = paddle1.move(0, 1)


    posX += speed[0]
    posY += speed[1]

    ballrect = ballrect.move(speed[0], speed[1])

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(white)
    screen.blit(ball, ballrect)
    screen.blit(player1, paddle1)

    pygame.display.flip()
