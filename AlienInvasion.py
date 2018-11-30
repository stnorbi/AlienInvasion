import sys
import pygame
from pygame.locals import RESIZABLE
from modules import settings, functions
from characters import ship



def run_game():
    #constructing the main window
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_width),RESIZABLE) # set the resolution
    pygame.display.set_caption("Alien Invasion") #set the window title

    #Adding the ship to the screen
    player_ship=ship.Ship(ai_settings,screen)

    # main loop
    while True:

        functions.event_checker(player_ship)
        player_ship.movement()
        functions.update_screen(ai_settings,screen,player_ship)


run_game()