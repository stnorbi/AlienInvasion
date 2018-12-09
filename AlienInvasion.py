import sys
import pygame
from pygame.locals import RESIZABLE
from modules import settings, functions
from characters import ship
from pygame.sprite import Group



def run_game():
    #constructing the main window
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_width),RESIZABLE) # set the resolution
    pygame.display.set_caption("Alien Invasion") #set the window title

    #Adding the ship to the screen
    player_ship=ship.Ship(ai_settings,screen)
    #enemy=ship.Alien(ai_settings,screen)
    bullets=Group()
    aliens=Group()

    # make the fleet visible
    functions.create_fleet(ai_settings, screen,player_ship, aliens)


    # main loop
    while True:

        functions.event_checker(ai_settings,screen,player_ship,bullets)
        player_ship.movement()
        functions.bullets_refresh(bullets)
        #functions.update_screen(ai_settings,screen,player_ship,enemy,bullets)
        functions.update_screen(ai_settings, screen, player_ship, aliens, bullets)



run_game()