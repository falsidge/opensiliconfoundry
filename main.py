import sys, pygame
pygame.init()

size = width, height = 800, 600
speed = [2, 2]
black = 0, 0, 0

screen = pygame.display.set_mode(size)

title_screen = pygame.image.load("images/sf_title.png")
title_screen_rect = title_screen.get_rect()

x
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            running = False
     



    screen.fill(black)
    screen.blit(title_screen, title_screen_rect)

    pygame.display.flip()
    pygame.time.delay(100)  