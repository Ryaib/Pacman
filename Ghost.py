#Paul Lindberg
#Assignment #4 Pacman
#Friday 9AM

from pygame.sprite import Sprite
import pygame
from spritesheet import Sheet


class Ghost(Sprite):
    def __init__(self, screen, name, center, settings):
        super(Ghost, self).__init__()
        self.screen = screen
        self.sheet = Sheet()
        self.name = name
        self.center = center
        self.settings = settings

        if self.name == 'Blinky':
            self.image = self.sheet.image(562, 0, 38, 38)

        if self.name == 'Inky':
            self.image = self.sheet.image(524, 0, 38, 38)

        if self.name == 'Pinky':
            self.image = self.sheet.image(486, 0, 38, 38)

        if self.name == 'Clyde':
            self.image = self.sheet.image(448, 0, 38, 38)

        self.image = pygame.transform.scale(self.image, (settings.block_width, settings.block_height))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.frame = 0
        self.ticks = 0

    def blitme(self):
        current = pygame.time.get_ticks()
        if current - self.ticks > 150:
            self.ticks = current
            self.animate()
        self.screen.blit(self.image, self.rect)

    def animate(self):
        if self.name == 'Blinky':
            if self.frame == 0:
                self.image = self.sheet.image(562, 0, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 1
                return
            if self.frame == 1:
                self.image = self.sheet.image(562, 38, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 0
                return
        elif self.name == 'Inky':
            if self.frame == 0:
                self.image = self.sheet.image(524, 0, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 1
                return
            if self.frame == 1:
                self.image = self.sheet.image(524, 38, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 0
                return
        elif self.name == 'Pinky':
            if self.frame == 0:
                self.image = self.sheet.image(486, 0, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 1
                return
            if self.frame == 1:
                self.image = self.sheet.image(486, 38, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 0
                return
        elif self.name == 'Clyde':
            if self.frame == 0:
                self.image = self.sheet.image(448, 0, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 1
                return
            if self.frame == 1:
                self.image = self.sheet.image(448, 38, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 0
                return
