import pygame
import os
import random
from classes import Backdrop, Button, Interactive, Window
pygame.init()
pygame.mixer.init()

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
screen_rect = screen.get_rect()
pygame.display.set_caption("Chilist")
font = pygame.font.Font("src\sysfont\sysfont\sysfont.ttf", 15)
done = False              
scene = 1
clock = pygame.time.Clock()
NEXT = pygame.USEREVENT + 1
vinylWindow_open = False
firstPlay = False
play = False
playlist = []
for filename in os.listdir(os.getcwd()+"\\src\\mus"):
    file = os.path.join(os.getcwd()+"\\src\\mus", filename)
    # checking if it is a file and that it's a music file
    if file.lower().endswith(('.mp3', '.wav', '.ogg')):
        playlist.append((file, filename))
playing = 0

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
            closeButton = Interactive(screen,"", x=840, y=75, w=54, h=50)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if vinylPlayer.rect.collidepoint(pygame.mouse.get_pos()) and vinylWindow_open == False: 
                    vinylWindow = Window(screen, "https://music.com/lofi")
                    vinylWindow_open = True
            if vinylWindow_open == True:
                vinylWindow = Window(screen, "https://music.com/lofi")
                control = Button(screen, "src/img/play.png", x=400, y=190)
                if event.type == pygame.MOUSEBUTTONDOWN and control.rect.collidepoint(pygame.mouse.get_pos()):
                    pygame.mixer.music.set_endevent(NEXT)
                    if not pygame.mixer.music.get_busy() and firstPlay == False:
                        control = Button(screen,"src/img/play.png", x=405, y=190)
                        currentlyplaying = random.choice(playlist)
                        pygame.mixer.music.load(currentlyplaying[0])
                        pygame.mixer.music.play()
                        clock.tick(10)
                        firstPlay, play = True, True
                    elif not pygame.mixer.music.get_busy():
                        pygame.mixer.music.unpause()
                        play = True
                    else:
                        pygame.mixer.music.pause()
                        play = False
                if event.type == NEXT:
                    currentlyplaying = random.choice(playlist)
                    pygame.mixer.music.load(currentlyplaying[0])
                    pygame.mixer.music.play()

                if play == False:
                    control = Button(screen,"src/img/play.png", x=405, y=190)
                else:
                    control = Button(screen,"src/img/pause.png", x=405, y=190)
                    currentlyplayins = font.render(f"Now playing: {currentlyplaying[1][:-4]}", False, (147, 133, 123), (251, 238, 208))
                    currentlyplayins_rect = currentlyplayins.get_rect(center=(520, 460)) #what this does is set the centre of the "now playing" text to the actual centre of the popup window
                    screen.blit(currentlyplayins, currentlyplayins_rect) # meaning that no matter how long the text is, it'll always be aligned to the centre.
                if keys[pygame.K_SPACE] or event.type == pygame.MOUSEBUTTONDOWN and closeButton.rect.collidepoint(pygame.mouse.get_pos()):
                    vinylWindow_open = False
    ##### Drawing code #####
    pygame.display.flip()
    clock.tick(60)
pygame.mixer.quit()
pygame.quit()
