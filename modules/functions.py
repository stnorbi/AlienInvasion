import pygame
import sys


def get_keydown_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.move_right=True
    elif event.key==pygame.K_LEFT:
        ship.move_left=True

def get_keyup_events(event,ship):
    if event.key==pygame.K_RIGHT:
        ship.move_right=False
    elif event.key==pygame.K_LEFT:
        ship.move_left=False


def event_checker(ship):
    for event in pygame.event.get(): # event loop
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type==pygame.KEYDOWN:
            get_keydown_events(event,ship)

        elif event.type==pygame.KEYUP:
            get_keyup_events(event,ship)


def update_screen(ai_settings,screen,ship):
    screen.fill(ai_settings.bg_color)  # fill the background by the selected colour
    ship.blitme()
    pygame.display.update()  # refreshing window