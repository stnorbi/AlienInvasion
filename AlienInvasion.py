import sys
import pygame
from pygame.locals import RESIZABLE
from modules import settings, functions
from characters import ship
from pygame.sprite import Group
from modules.gameStats import GameStats


def run_game():
    #constructing the main window
    pygame.init()
    ai_settings=settings.Settings()
    screen=pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_width),RESIZABLE) # set the resolution
    pygame.display.set_caption("Alien Invasion") #set the window title

    stats=GameStats(ai_settings)

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

        if stats.game_active:
            player_ship.movement()
            functions.bullets_refresh(ai_settings,screen,player_ship,aliens,bullets)
            functions.update_aliens(ai_settings,stats,screen,player_ship,aliens,bullets)
            functions.update_screen(ai_settings, screen, player_ship, aliens, bullets)



run_game()