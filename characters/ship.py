import pygame
import os
from pygame.sprite import Sprite

ICONPATH=os.path.dirname(__file__).replace('characters','icons') + "/"


class Ship():
    def __init__(self,ai_settings,screen):
        # set up the ship and its position
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load(ICONPATH + "ship.bmp")
        self.rect=self.image.get_rect() #rectangle of the ship
        self.screen_rect=screen.get_rect() #rectangel of the screen

        #set the ship in the bottom of the screen
        self.rect.centerx=self.screen_rect.centerx #set the rectangle to middle
        self.rect.bottom=self.screen_rect.bottom  #set rectangle to bottom

        self.center=float(self.rect.centerx)
        print(self.rect.centerx)

        # moving tag
        self.move_right=False
        self.move_left=False

    def center_ship(self):
        self.center=self.screen_rect.centerx

    def movement(self):

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx+=self.ai_settings.ship_speed

        if self.move_left and self.rect.left > 0:
            self.rect.centerx-=self.ai_settings.ship_speed


    def blitme(self):
        self.screen.blit(self.image,(self.rect[0],self.rect[1])) #makes the ship visible

class Alien(Sprite):
    """The class of an alien"""

    def __init__(self,ai_settings,screen):
        super(Alien,self).__init__()
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load(ICONPATH + "alien.bmp")
        self.rect=self.image.get_rect()

        self.rect.x=self.rect.width
        self.rect.y=self.rect.height

        self.x=float(self.rect.x)

    def edge_checker(self):
        screen_rect=self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    # it assures the movement of the alien fleet. "update" function is inherited from the "Sprite" class
    def update(self):
        self.x += (self.ai_settings.alien_speed * self.ai_settings.fleet_direct)
        self.rect.x=self.x

    def blitme(self):
        self.screen.blit(self.image,self.rect)