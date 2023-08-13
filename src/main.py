import pygame
from classes import Backdrop, Button, Interactive, Window
pygame.init()

##### Colours #####
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
RED   = (255,   0,   0)
BLUE  = (  0,   0, 255)

##### Screen Initialisation #####
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Chilist")
done = False              
scene = 1
clock = pygame.time.Clock()
vinylWindow_open = False
##### Main Program Loop #####
while not done:
    ##### Events Loop #####
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        ##### Logic #####
        # This code retrieves coordinates of mouse clicks, which I need to test the colliders.
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            print(x,y)
        keys = pygame.key.get_pressed()
        if scene == 1:
            backdrop = Backdrop(screen, "src/img/roomlinesSUNRISE.png")
            bountiesPoster = Interactive(screen, "[!] A bounties poster.", x=46, y=39, w=190, h=238)
            vinylPlayer = Interactive(screen, "[!] A vinyl player.", x=294, y=261, w=152, h=158)
            calendar = Interactive(screen,"[!] A calendar.", x=327, y=38, w=221, h=178)
            if event.type == pygame.MOUSEBUTTONDOWN:
                while vinylPlayer.rect.collidepoint(pygame.mouse.get_pos()) and vinylWindow_open == False: 
                    vinylWindow = Window(screen, "Vinyl")
                    vinylWindow_open = True
            if keys[pygame.K_SPACE]:
                vinylWindow_open = False
    ##### Drawing code #####
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
