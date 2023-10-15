import pygame
import os
import random
import json
import math
import pygame_textinput
import datetime
import shutil
from time import localtime, strftime
from classes import Backdrop, Button, Interactive, Window, pomoTimer
from classes import multiline, checkClick, tooltip, dump, notify
pygame.init()
pygame.mixer.init()

##### Screen Initialisation #####
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 576
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
screen = pygame.display.set_mode(size)
screen_rect = screen.get_rect()
pygame.display.set_caption("Chilist")
font = pygame.font.Font("src\sysfont\sysfont\sysfont.ttf", 15)
task_font = pygame.font.Font("src\sysfont\sysfont\sysfont.ttf", 20)
title_font = pygame.font.Font("src\sysfont\sysfont\sysfont.ttf", 25)
pygame.display.set_icon(pygame.image.load(r"src\img\favicon.png"))
done = False              
scene = 0
clock = pygame.time.Clock()

##### EVENTS #####
NEXT = pygame.USEREVENT + 1
TIMER = pygame.USEREVENT + 2 
vinylWindow_open, calendar_open, todoTimer_open, firstPlay, play, placed, timer_running = False, False, False, False, False, False, False
study = True

pygame.time.set_timer(TIMER, 1000)


##### OBJECTS #####
# make playlist out of existing mp3 files
default_dir = f"C:/Users/{os.getlogin()}/Documents/Chillist"
if not os.path.exists(default_dir):
    os.makedirs(default_dir)
if not os.path.exists(default_dir + "/mus"):
    os.makedirs(default_dir + "/mus")
if os.listdir(default_dir +"/mus") == []:
    for filename in os.listdir(os.getcwd()+"\\src\\mus"):
        file = os.path.join(os.getcwd()+"\\src\\mus", filename)
        if file.lower().endswith(('.mp3', '.wav', '.ogg')):
            shutil.copyfile(file, default_dir + "/mus/" + filename)
if not os.path.exists(default_dir + "/settings.json"):
    dump({
    "settings": [
        {
            "pomotimer": [
                1500,
                300
            ],
            "completed_tasks": 0
        }
    ],
    "stickers": []
}, default_dir + "/settings.json")


playlist = []
for filename in os.listdir(default_dir +"/mus"):
    file = os.path.join(default_dir + "/mus/", filename)
    # checking if it is a file and that it's a music file
    if file.lower().endswith(('.mp3', '.wav', '.ogg')):
        playlist.append((file, filename))

##### LOAD SETTINGS #####
with open(default_dir + "/settings.json") as json_file:
    save = json.load(json_file)
    json_file.close()
stickers = save["stickers"]
settings = save["settings"]
interval = save["settings"][0]["pomotimer"]
counter = interval[0]

    
# collate date and time using os
attributes = {"username": os.getlogin(),
              "month": strftime("%B", localtime()),
              "day_name": strftime("%A", localtime()),
              "day_date": strftime("%d", localtime()),
              "time":  (strftime("%H", localtime()), strftime("%M", localtime()))
              }
boundaries = [(0,12, "morning"), (12, 17, "afternoon"), (17, 20, "evening"), (20, 24, "night")] # these are the defined hour boundaries in 24 hour time for what constitutes  day, afternoon, evening or  night (imo)
attributes["time_period"] = [boundary[2] for boundary in boundaries if boundary[0] <= int(attributes["time"][0]) < boundary[1]][0]
textinput = pygame_textinput.TextInputVisualizer(font_object=font, font_color=(255,255,255), cursor_color=(255,255,255))

##### FUNCTIONS FOR THIS FILE ONLY #####
def nextsong():
    currentlyplaying = random.choice(playlist)
    pygame.mixer.music.load(currentlyplaying[0])
    pygame.mixer.music.play()

##### Main Program Loop #####
while not done:
    ##### Events Loop #####
    clock.tick(60)
    event_list = pygame.event.get()
    for event in event_list:
        if event.type == pygame.QUIT:
            done = True
        ##### Logic #####
        # This code retrieves coordinates of mouse clicks, which I need to test the colliders.
        if event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
        if event.type == NEXT:
            nextsong()
        keys = pygame.key.get_pressed()
    if scene == 0: 
        if attributes["time_period"] == "afternoon" or attributes["time_period"] == "evening":
            backdrop = Backdrop(screen, "src/img/afternoon.png")
            multiline(screen, [f"Good {attributes['time_period']}, {attributes['username']}.", f"It is {attributes['day_name']}, {attributes['month']} {attributes['day_date']}"], title_font, "center", colour=(22,9,55), x=520, y=180, w=20)
        else: 
            backdrop = Backdrop(screen, f"src/img/{attributes['time_period']}.png")
            multiline(screen, [f"Good {attributes['time_period']}, {attributes['username']}.", f"It is {attributes['day_name']}, {attributes['month']} {attributes['day_date']}"], title_font, "center", x=520, y=180, w=20)
        if event.type == pygame.MOUSEBUTTONDOWN:
            scene = 1
            
    
    elif scene == 1:
        backdrop = Backdrop(screen, "src/img/roomlinesSUNRISE.png")
        todoTimer = Interactive(screen, "[!] A timer.", x=46, y=39, w=190, h=238)
        vinylPlayer = Interactive(screen, "[!] A vinyl player.", x=294, y=261, w=152, h=158)
        calendar = Interactive(screen,"[!] A calendar.", x=327, y=38, w=221, h=178)
        closeButton = Interactive(screen,"", x=840, y=75, w=54, h=50)
        if vinylWindow_open == False and calendar_open == False and todoTimer_open == False: 
            if checkClick(vinylPlayer, pygame.mouse.get_pos(), event_list):
                vinylWindow_open = True
            if checkClick(calendar, pygame.mouse.get_pos(), event_list):
                calendar_open = True
            if checkClick(todoTimer, pygame.mouse.get_pos(), event_list):
                todoTimer_open = True

        if vinylWindow_open == True:
            vinylWindow = Window(screen, "https://music.com/lofi")
            control = Button(screen, "src/img/play.png", x=400, y=190)
            if checkClick(control, pygame.mouse.get_pos(), event_list):
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
            if play == False:
                control = Button(screen,"src/img/play.png", x=405, y=190)
            else:
                control = Button(screen,"src/img/pause.png", x=405, y=190)
                currentlyplaying_text = font.render(f"Now playing: {currentlyplaying[1][:-4]}", False, (147, 133, 123), (251, 238, 208))
                currentlyplayins_rect = currentlyplaying_text.get_rect(center=(520, 460)) #what this does is set the centre of the "now playing" text to the actual centre of the popup window
                screen.blit(currentlyplaying_text, currentlyplayins_rect) # meaning that no matter how long the text is, it'll always be aligned to the centre.   


        elif calendar_open == True:
            calendarWindow = Window(screen, "https://eisenhower.com/matrix")
            matrix = Interactive(screen, "", img="src/img/matrixmockup.png", x=159, y=148, w=700, h=294)
            matrixlabel = Interactive(screen, "", img="src/img/matrixlabel.png",x=159, y=451)
            trashBin = Interactive(screen, "Delete All", font=task_font, x=831, y=459, w=27, h=27)
            if checkClick(matrix, pygame.mouse.get_pos(), event_list):
                placed = True
                stickerChoice = random.choice(
                    ["circle",
                        "diamond",
                        "heart",
                        "star"])
            if placed == True:
                textinput.update(event_list)
                screen.blit(textinput.surface, (179, 465))
                if event.type == pygame.KEYDOWN and event.key == pygame.K_RETURN:
                    stickers.append({
                        "coords": [x,y], 
                        "desc": textinput.value,
                        "shape": stickerChoice,
                        "boxpos": [600, 227+40*(len(stickers))],
                        "placed": False
                    })
                    matrixlabel = Interactive(screen, "", img="src/img/matrixlabel.png",x=159, y=451)
                    textinput = pygame_textinput.TextInputVisualizer(font_object=font, font_color=(255,255,255), cursor_color=(255,255,255))
                    placed = False
            for i in stickers:
                tooltip(screen, "src/img/"+i["shape"]+".png", task_font, i["desc"], x=i["coords"][0], y=i["coords"][1])
            if checkClick(trashBin, pygame.mouse.get_pos(), event_list):
                stickers = []

        elif todoTimer_open == True:
            todoTimerWindow = Window(screen, "https://todolist.com/pomodorotimer")
            todolayout = Interactive(screen, "", img="src/img/timermockup.png", x=130, y=130)
            control = Button(screen, "src/img/play_xs.png", x=284, y=431)
            restart = Button(screen, "src/img/restart.png", x=401, y=431)
            pygame.draw.circle(screen,(255, 251, 226),(360,310), 110)
            timer = pomoTimer(screen)

            if study == True:
                timer.draw(screen, ((counter/interval[0])*2*math.pi)+math.pi/2)
            else: 
                timer.draw(screen, ((counter/interval[1])*2*math.pi)+math.pi/2)
            timer_text = title_font.render(str(datetime.timedelta(seconds=counter))[2:], True, (147, 133, 123))
            screen.blit(timer_text, timer_text.get_rect(center = (360,450)))

            if checkClick(control, pygame.mouse.get_pos(), event_list):
                if timer_running == False:
                    timer_running = True
                else:
                    timer_running = False

            if timer_running == True:
                control = Button(screen, "src/img/pause_xs.png", x=284, y=431)
            else:
                control = Button(screen, "src/img/play_xs.png", x=284, y=431)
            if stickers:
                multiline(screen, [i["desc"] if len(i["desc"]) < 19 else i["desc"][:16]+"..." for i in stickers[:6]], title_font, "topleft", colour=(202, 182, 169), x=635, y=230, w=20)
                for sticker in stickers:
                    if stickers.index(sticker) <= 5:         
                        checkbox_rect = Interactive(screen, "", img="src/img/checkboxes.png", x=sticker["boxpos"][0], y=227+40*(stickers.index(sticker)))
                        if checkClick(checkbox_rect, pygame.mouse.get_pos(), event_list):
                            sticker["placed"] = True
                        if sticker["placed"] == True:
                            settings[0]["completed_tasks"] += 1
                            screen.blit(pygame.image.load("src/img/cross.png"), pygame.image.load("src/img/cross.png").get_rect(topleft=(sticker["boxpos"][0], 227+40*(stickers.index(sticker)))))
                            del stickers[stickers.index(sticker)]
            else: 
                multiline(screen, ["No tasks! :)", "Try adding some using", "the Eisenhower matrix."], task_font, "topleft", colour=(202, 182, 169), x=615, y=230, w=10)
        if timer_running == True:
            if checkClick(restart, pygame.mouse.get_pos(), event_list):
                if study == True:
                    counter = interval[0]
                else: 
                    counter = interval[1]
            for event in event_list:
                if event.type == TIMER:
                    counter -= 1
                    if counter == 0:
                        if study == True:
                            study = False
                            counter = interval[1]
                            notify("BREAK", f"Take a break for the next {str(datetime.timedelta(seconds=interval[1]))[2:-3]} minutes. You've earned it!")
                        else: 
                            study = True
                            counter = interval[0]
                            notify("STUDY", f"It's time to study for the next {str(datetime.timedelta(seconds=interval[0]))[2:-3]} minutes. Keep up the good work!")
        if checkClick(closeButton, pygame.mouse.get_pos(), event_list):
            calendar_open, vinylWindow_open, todoTimer_open = False, False, False

    ##### Drawing code #####
    pygame.display.flip()
    clock.tick(60)
dump({
    "settings": settings,
    "stickers": stickers}, default_dir + "/settings.json")
pygame.mixer.quit()
pygame.quit()
