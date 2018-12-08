import pygame
import sys
from characters import ammo
from characters.ship import Alien


def create_fleet(ai_settings, screen,aliens):
    """Setting up the fleet of the Aliens"""
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    available_sp_x=ai_settings.screen_width - 2 *alien_width
    nr_aliens_x=int(available_sp_x / (2*alien_width))

    for alien_nr in range(nr_aliens_x):
        alien = Alien(ai_settings,screen)
        alien.x=alien_width + 2 * alien_width * alien_nr
        alien.rect.x=alien.x
        aliens.add(alien)


def get_keydown_events(event,ai_settings, screen,ship,bullets):

    if event.key==pygame.K_RIGHT:
        ship.move_right=True

    elif event.key==pygame.K_LEFT:
        ship.move_left=True

    elif event.key == pygame.K_SPACE:
        bullet_firing(ai_settings,screen,ship,bullets)

    elif event.key==pygame.K_q:
        sys.exit()


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


def update_screen(ai_settings,screen,ship,alien, bullets):
    pygame.display.update()  # refreshing window (before everything)

    # fill the background by the selected colour. Use after screen update
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.setBullet()

    ship.blitme()
    alien.draw(screen) #  draw is the attribute of Group. Group does not have "blit" method

    pygame.display.flip()

def bullets_refresh(bullets):
    bullets.update()

    # deleting the invisible bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) #Remove function is inherited from SpriteS