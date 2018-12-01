import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self,ai_settings,screen,ship):
        super(Bullet,self).__init__()
        self.screen=screen

        #set the place of the bullet
        self.rect=pygame.Rect(0,0,ai_settings.bullet_w,
                              ai_settings.bullet_h)
        self.rect.centerx=ship.rect.centerx
        self.rect.top=ship.rect.top

        self.y=float(self.rect.y)

        #set the colour of the bullet
        self.color=ai_settings.bullet_c

        #set the speed to the bullet
        self.speed_fact=ai_settings.bullet_speed

    # inherited function from Sprite
    def update(self):
        self.y -= self.speed_fact
        self.rect.y=self.y
        print(self.rect)

    def setBullet(self):
        pygame.draw.rect(self.screen,self.color,self.rect)