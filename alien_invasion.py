import pygame
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf
from pygame.sprite import Group

def run_game():

    # Initialize game and create a screen object.
    pygame.init()

    ai_settings = Settings()

    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    
    pygame.display.set_caption("Alien Invasion")

    # Make a ship.
    ship = Ship(ai_settings,screen)
    # Make a group to store bullets in.
    bullets = Group()
    # Make an alien.
    alien = Alien(ai_settings, screen)

    # Start the main loop for game.
    while True:
        gf.check_events(ai_settings, screen, ship, bullets)
        gf.update_screen(ai_settings, screen, ship, alien, bullets)
        

run_game()