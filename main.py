import sys, pygame
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

title_screen = pygame.image.load("images/sf_title.png")
title_screen_rect = title_screen.get_rect()

ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
        elif event.type == pygame.VIDEORESIZE:


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen.fill(black)
    screen.blit(title_screen, title_screen_rect)
    screen.blit(ball, ballrect)
    pygame.display.flip()
    pygame.time.delay(100)  