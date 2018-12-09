import pygame
import sys
from characters import ammo
from characters.ship import Alien
from time import sleep


def check_bottom_aliens(ai_settings,stats,screen,ship,aliens,bullets):
    screen_rect=screen.get_rect()
    for alien in aliens.sprites():
        if alien.rect.bottom >= screen_rect.bottom:
            ship_hit(ai_settings, stats,screen,ship, aliens, bullets)
            break


def ship_hit(ai_settings,stats,screen,ship,aliens,bullets):
    """Ship death"""

    if stats.ships_left>0:
        stats.ships_left-=1

    else:
        stats.game_active=False

    # Make the alien and bullets group empty
    aliens.empty()
    bullets.empty()

    create_fleet(ai_settings,screen,ship,aliens)
    ship.center_ship()

    sleep(0.5)

def change_fleet_direct(ai_settings,aliens):
    for alien in aliens.sprites():
        alien.rect.y += ai_settings.fleet_down_speed

    ai_settings.fleet_direct *= -1


def fleet_edge_checker(ai_settings,aliens):

    for alien in aliens.sprites():
        if alien.edge_checker():
            change_fleet_direct(ai_settings,aliens)
            break

def update_aliens(ai_settings, stats, screen, ship, aliens, bullets):
    """Position update for the alien fleet"""

    fleet_edge_checker(ai_settings,aliens)
    aliens.update()

    check_bottom_aliens(ai_settings,stats,screen,ship,aliens,bullets)


    # spritecollideany: The method looks for any member of the group that’s collided with
    # the sprite and stops looping through the group as soon as it finds one mem-
    # ber that has collided with the sprite.

    if pygame.sprite.spritecollideany(ship,aliens):
        ship_hit(ai_settings, stats, screen, ship, aliens, bullets)


def get_nr_rows(ai_settings,ship_height, alien_height):
    """Assure how many alien line is visible on the screen"""
    available_sp_y=ai_settings.screen_height - 3*alien_height - ship_height
    nr_rows=int(available_sp_y/(2*alien_height))
    return nr_rows

def get_nr_aliens_x(ai_settings, alien_width):
    """Number of aliens in a line"""
    available_sp_x=ai_settings.screen_width - 2*alien_width
    nr_aliens_x=int(available_sp_x/(2*alien_width))
    return nr_aliens_x

def create_alien(ai_settings,screen,aliens,alien_nr, row_nr):
    """Create an alien instance"""
    alien=Alien(ai_settings,screen)
    alien_width=alien.rect.width
    alien.x = alien_width + 2 * alien_width * alien_nr
    alien.rect.x = alien.x
    alien.rect.y=alien.rect.height + 2*alien.rect.height * row_nr
    aliens.add(alien)

def create_fleet(ai_settings, screen,ship,aliens):
    """Setting up the fleet of the Aliens"""
    alien=Alien(ai_settings,screen)
    nr_aliens_x=get_nr_aliens_x(ai_settings,alien.rect.width)
    nr_rows=get_nr_rows(ai_settings,ship.rect.height,alien.rect.height)

    for row_nr in range(nr_rows):
        for alien_nr in range(nr_aliens_x):
            create_alien(ai_settings,screen,aliens,alien_nr,row_nr)


def get_keydown_events(event,ai_settings, screen,ship,bullets):
    """Check which button has been pressed"""

    if event.key==pygame.K_RIGHT:
        ship.move_right=True

    elif event.key==pygame.K_LEFT:
        ship.move_left=True

    elif event.key == pygame.K_SPACE:
        bullet_firing(ai_settings,screen,ship,bullets)

    elif event.key==pygame.K_q:
        sys.exit()


def get_keyup_events(event,ship):
    """Check which button has been released"""

    if event.key==pygame.K_RIGHT:
        ship.move_right=False

    elif event.key==pygame.K_LEFT:
        ship.move_left=False


def event_checker(ai_settings,screen,ship, bullets):
    """Control the event of the buttons"""

    for event in pygame.event.get(): # event loop

        if event.type == pygame.QUIT:
            sys.exit()

        elif event.type==pygame.KEYDOWN:
            get_keydown_events(event,ai_settings,screen,ship,bullets)


        elif event.type==pygame.KEYUP:
            get_keyup_events(event,ship)


def bullet_firing(ai_settings, screen, ship, bullets):
    """Fire action from the player's ship"""

    if len(bullets) < ai_settings.bullets_nr:
        new_bullet = ammo.Bullet(ai_settings, screen, ship)
        bullets.add(new_bullet)


def update_screen(ai_settings,screen,ship,alien, bullets):
    """General screen update"""
    pygame.display.update()  # refreshing window (before everything)

    # fill the background by the selected colour. Use after screen update
    screen.fill(ai_settings.bg_color)

    for bullet in bullets.sprites():
        bullet.setBullet()

    ship.blitme()
    alien.draw(screen) #  draw is the attribute of Group. Group does not have "blit" method

    pygame.display.flip()

def bullets_refresh(ai_settings,screen,ship,aliens,bullets):
    """Assure the movement of the bullets"""
    bullets.update()


    # deleting the invisible bullets
    for bullet in bullets.copy():
        if bullet.rect.bottom <= 0:
            bullets.remove(bullet) #Remove function is inherited from SpriteS

    alien_bullet_collisions(ai_settings,screen,ship,aliens,bullets)


def alien_bullet_collisions(ai_settings,screen,ship,aliens,bullets):
    # Whenever the rect of a bullet and alien overlap, groupcollide() adds a key-value pair to the dictionary it returns.
    collisions = pygame.sprite.groupcollide(bullets, aliens, True, True)

    if len(aliens)==0:
        bullets.empty()
        create_fleet(ai_settings,screen,ship,aliens)