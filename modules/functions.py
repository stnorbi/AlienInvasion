import pygame
import sys
from characters import ammo

def get_keydown_events(event,ai_settings, screen,ship,bullets):

    if event.key==pygame.K_RIGHT:
        ship.move_right=True

    elif event.key==pygame.K_LEFT:
        ship.move_left=True

    elif event.key == pygame.K_SPACE:
        bullet_firing(ai_settings,screen,ship,bullets)


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


def bullet_firing(ai_settings, screen, ship, bullets):
    if len(bullets) < ai_settings.bullets_nr:
        new_bullet = ammo.Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings,screen,ship, bullets):
    pygame.display.update()  # refreshing window (before everything)

    # fill the background by the selected colour. Use after screen update
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.setBullet()

    ship.blitme()

def bullets_refresh(bullets):
    bullets.update()

    # deleting the invisible bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet)