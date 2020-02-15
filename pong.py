import pygame, sys

pygame.init()

size =  width, height = 480, 640
speed = [1,1]
position = posX, posY = 0, 0
black = 255,255,255

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

screen = pygame.display.set_mode(size)

#while True:
for x in range(0,10):

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()


    posX += speed[0]
    posY += speed[1]


    #TODO figure out slowing down speed
    print("posX:  ", posX)
    print("posY:  ", posY)
    print("ballrect:  ", ballrect.left)

    ballrect = ballrect.move(speed[0], speed[1])

    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]


    screen.fill(black)
    screen.blit(ball, ballrect)

    pygame.display.flip()
