import pygame
import os

ICONPATH=os.path.dirname(__file__).replace('characters','icons') + "/"


class Ship():
    def __init__(self,screen):
        # set up the ship and its position
        self.screen=screen

        self.image=pygame.image.load(ICONPATH + "ship.bmp").convert()
        self.rect=self.image.get_rect() #rectangle of the ship
        self.screen_rect=screen.get_rect() #rectangel of the screen

        #set the ship in the bottom of the screen
        self.rect.centerx=self.screen_rect.centerx #set the rectangle to middle
        self.rect.bottom=self.screen_rect.bottom  #set rectangle to bottom

        self.move_right=False #moving tag
        self.move_left=False



    def movement(self):

        if self.move_right:
            self.rect.centerx+=1

        if self.move_left:
            self.rect.centerx-=1


    def blitme(self):
        self.screen.blit(self.image,(self.rect[0],self.rect[1])) #makes the ship visible

