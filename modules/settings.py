class Settings():
    """The current class store the the settings of the gam"""

    def __init__(self):
        #Display settings
        self.screen_width=800
        self.screen_height=700
        self.bg_color=(230,230,230)

        # Player ship settings
        self.ship_speed=1.5

        # Bullet settings
        self.bullet_speed=3
        self.bullet_w=3
        self.bullet_h=15
        self.bullet_c=60,60,60
        self.bullets_nr=3

        # Alien settings
        self.alien_speed=1
        self.fleet_down_speed=2
        self.fleet_direct=1 # "1" indicates right; "-1" indicates left movement






