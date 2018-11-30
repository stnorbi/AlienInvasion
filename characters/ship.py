import pygame

class Ship():
    def __init__(self,screen):
        # set up the ship and its position
        self.screen=screen

        self.image=pygame.image.load("icons/ship.bmp")
        self.rect=self.image.get_rect() #rectangle of the ship
        self.screen_rect=screen.get_rect() #rectangel of the screen

        #set the ship in the bottom of the screen
        self.rect.centerx=self.screen_rect.centerx #set the rectangle to middle
        self.rect.bottom=self.screen_rect.bottom  #set rectangle to bottom

    def blitme(self):
        self.screen.blit(self.image, self.rect) #makes the ship visible


