import sys
import pygame

def check_events():
    """Respond to events like key press and mouse click"""
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            print('Exiting the game')
            sys.exit()

def update_screen(ai_settings, screen, ship):
    """Update images on the screen and flip to new screen"""
    # Redraw the screen during each pass through the loop
    screen.fill(ai_settings.bg_color)
    ship.blitme()

    # Make the most recently drawn screen visible
    pygame.display.flip()