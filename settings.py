class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (0, 0, 0)

        # Ship settings
        self.ship_speed_factor = 1.2

        # Bullet settings
        self.bullet_speed_factor = 1
        self.bullet_width = 2
        self.bullet_height = 20
        self.bullet_color = 250, 0, 0
        self.bullets_allowed  = 3