import pygame
pygame.init()
import json
import math
import sys
import os
from notifypy import Notify
#general
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)

font = pygame.font.Font(resource_path("sysfont\sysfont\sysfont.ttf"), 30)
smallfont = pygame.font.Font(resource_path("sysfont\sysfont\sysfont.ttf"), 15)
class Backdrop():
    def __init__(self, screen, img, x=0, y=0, ):
        """
        Initialises the backdrop. Accepts backdrop image and coordinate location [default is (0,0)]
        """

        self.rect = pygame.image.load(img).get_rect(topleft = (x,y))
        screen.blit(pygame.image.load(img), (x,y))

class Button():
    def __init__(self, screen, img, x=0, y=0):
        """
        Initialises the button. Accepts button image and coordinate location [default is (0,0)]
        """
        self.rect = pygame.image.load(img).get_rect(topleft = (x,y))
        screen.blit(pygame.image.load(img), (x,y))

class Interactive():
    def __init__(self, screen, tooltip, img="", font=font, colour=(148,133,123), x=0, y=0, w=50, h=50):
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

class Window():
    def __init__(self, screen, title, size="large", x=128, y=72):
        if size == "large":
            screen.blit(pygame.image.load(resource_path("img/window.png")), (x,y))
        self.title = smallfont.render(title, False, (255, 255, 255))
        screen.blit(self.title, (158, 95))

class pomoTimer():
    def __init__(self, screen, radius = 110, width = 75, ring_colour=(202, 183, 170)):
        self.screen = screen
        self.radius = radius
        self.width = width
        self.ring_colour = ring_colour
    def draw(self, screen, end_angle):
        arc_rect = pygame.Rect(0,0, self.radius*2, self.radius*2)
        arc_rect.center = (360,310)
        pygame.draw.arc(screen, self.ring_colour, arc_rect, math.pi/2, end_angle, self.width)

def multiline(screen, lines, font, pos, colour=(0,0,0), x=0, y=0, w=2): 
    """
    Takes a list containing strings and creates a surface where all strings are blitted one below the other.
    Currently supports custom line spacing, font object (new font sizes need to be specified external of function use) and position (only top-left and center right now)

    """
    label = []
    for line in lines: 
        label.append(font.render(line, True, colour))
    if pos == "center":
        for line in range(len(label)):
            screen.blit(label[line],(label[line]).get_rect(center=(x,y+(line*20)+(w*line))))
    elif pos == "topleft":
        for line in range(len(label)):
            screen.blit(label[line],(label[line]).get_rect(topleft=(x,y+(line*20)+(w*line))))

def checkClick(item, mouse_pos, event_list):
    for event in event_list:
        if event.type == pygame.MOUSEBUTTONDOWN and item.rect.collidepoint(mouse_pos):
            return True

def tooltip(screen, img, font, tooltip, colour=(148,133,123), x=0,y=0):
    rect = pygame.image.load(img).get_rect(center = (x,y))
    screen.blit(pygame.image.load(img), rect)
    tooltip= font.render(tooltip, False, (255, 255, 255), colour)
    if rect.collidepoint(pygame.mouse.get_pos()): 
        mouse_pos = pygame.mouse.get_pos()
        screen.blit(tooltip, (mouse_pos[0]+16, mouse_pos[1]))
######
def notify(title, message):
    notification = Notify(
        default_notification_title=title,
        default_notification_application_name="Chillist",
        default_notification_icon=resource_path("img/favicon.png"),
    )
    notification.message = message
    notification.send()

def dump(settings, file):
    with open(file, "w") as json_file: 
        json.dump(
            settings, json_file, indent=4)
        json_file.close()
