import sys
import pygame
from modules import settings

def run_game():
    #constructing the main window
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_width)) # set the resolution
    pygame.display.set_caption("Alien Invasion") #set the window title


    # main loop
    while True:

        for event in pygame.event.get(): #event loop
            if event.type==pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.bg_color) #fill the background by the selected colour

        pygame.display.flip() #refreshing window

run_game()