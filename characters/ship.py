import pygame
import os

ICONPATH=os.path.dirname(__file__).replace('characters','icons') + "/"


class Ship():
    def __init__(self,ai_settings,screen):
        # set up the ship and its position
        self.screen=screen
        self.ai_settings=ai_settings

        self.image=pygame.image.load(ICONPATH + "ship.bmp").convert()
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


    def movement(self):

        if self.move_right and self.rect.right < self.screen_rect.right:
            self.rect.centerx+=self.ai_settings.ship_speed

        if self.move_left and self.rect.left > 0:
            self.rect.centerx-=self.ai_settings.ship_speed


    def blitme(self):
        self.screen.blit(self.image,(self.rect[0],self.rect[1])) #makes the ship visible

