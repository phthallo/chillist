import pygame
pygame.init()
#general
font = pygame.font.Font("src\sysfont\sysfont\sysfont.ttf", 30)
class Backdrop():
    def __init__(self, screen, img, x=0, y=0):
        """
        Initialises the backdrop. Accepts backdrop image and coordinate location [default is (0,0)]
        """
        self.rect = pygame.image.load(img).get_rect(topleft = (x,y))
        screen.blit(pygame.image.load(img), (x,y))

class Button():
    def __init__(self, screen, img="", x=0, y=0):
        """
        Initialises the button. Accepts button image and coordinate location [default is (0,0)]
        For now, the img is optional while I try to figure out how to generate buttons better.
        """
        self.rect = pygame.image.load(img).get_rect(topleft = (x,y))
        screen.blit(pygame.image.load(img), (x,y))

class Interactive():
    def __init__(self, screen, tooltip, img="", colour=(148,133,123), x=0, y=0, w=50, h=50):
        """
        Initialises the interactive class, which can refer to either a placed image or an invisible rect.
        This is done considering that the pre-existing interactives are part of the background image,
        whereas new unlockable interactives will be placed images. 
        """
        if img:
            self.rect = pygame.image.load(img).get_rect(topleft = (x,y))
            screen.blit(pygame.image.load(img), (x,y))
        else:
            self.rect = pygame.Rect((x,y), (w,h))
        self.tooltip= font.render(tooltip, False, (255, 255, 255), colour)
        if self.rect.collidepoint(pygame.mouse.get_pos()): 
            mouse_pos = pygame.mouse.get_pos()
            screen.blit(self.tooltip, (mouse_pos[0]+16, mouse_pos[1]))