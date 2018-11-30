import sys
import pygame
from pygame.locals import RESIZABLE
from modules import settings
from characters import ship


def run_game():
    #constructing the main window
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_width),RESIZABLE) # set the resolution
    pygame.display.set_caption("Alien Invasion") #set the window title

    #Adding the ship to the screen
    player_ship=ship.Ship(screen)

    # main loop
    while True:

        for event in pygame.event.get(): #event loop
            if event.type==pygame.QUIT:
                sys.exit()

        player_ship.blitme()

        screen.fill(ai_settings.bg_color) #fill the background by the selected colour


        pygame.display.flip() #refreshing window


run_game()