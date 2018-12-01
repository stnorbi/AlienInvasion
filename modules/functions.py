import pygame
import sys
from characters import bull

def get_keydown_events(event,ai_settings, screen,ship,bullets):

    if event.key==pygame.K_RIGHT:
        ship.move_right=True

    elif event.key==pygame.K_LEFT:
        ship.move_left=True

    elif event.key == pygame.K_SPACE:
        new_bullet = bull.Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)

def get_keyup_events(event,ship):

    if event.key==pygame.K_RIGHT:
        ship.move_right=False

    elif event.key==pygame.K_LEFT:
        ship.move_left=False


def event_checker(ai_settings,screen,ship, bullets):
    for event in pygame.event.get(): # event loop

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            get_keydown_events(event,ai_settings,screen,ship,bullets)


        elif event.type==pygame.KEYUP:
            get_keyup_events(event,ship)




def update_screen(ai_settings,screen,ship, bullets):
    screen.fill(ai_settings.bg_color)  # fill the background by the selected colour
    pygame.display.update()  # refreshing window

    for bullet in bullets.sprites():
        bullet.setBullet()

    ship.blitme()

