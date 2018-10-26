#Paul Lindberg
#Assignment #4 Pacman
#Friday 9AM

import pygame


class Sheet:
    def __init__(self):
        self.sprite_sheet = pygame.image.load('SPRITE_SHEET.PNG').convert()

    def image(self, x, y, width, height):
        """ Grab a single image out of a larger spritesheet
            Pass in the x, y location of the sprite
            and the width and height of the sprite. """

        # Create a new blank image
        image = pygame.Surface([width, height])

        # Copy the sprite from the large sheet onto the smaller image
        image.blit(self.sprite_sheet, (0, 0), (x, y, width, height))

        # Return the image
        return image
