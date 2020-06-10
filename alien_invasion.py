
import pygame

from settings import Settings
from ship import Ship
import game_functions as gf

def run_game():
    # Initialize pygame, settings and screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien Invasion')

    # Create ship
    ship = Ship(screen)

    # Main loop of the game
    while True:

        # Watch for player events
        gf.check_events()

        gf.update_screen(ai_settings, screen, ship)


run_game()