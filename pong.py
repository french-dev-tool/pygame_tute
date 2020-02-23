import pygame, sys

pygame.init()

size =  width, height = 480, 640
speed = [1,1]
position = posX, posY = 0, 0
white = 255,255,255
PADDLE_H = 25
PADDLE_W = 5

paddle1 = pygame.Rect((2,2), (200,250))

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

screen = pygame.display.set_mode(size)
player1 = pygame.Surface((20,200))
player1.fill((200,200,200))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


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
