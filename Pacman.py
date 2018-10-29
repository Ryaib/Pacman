#Paul Lindberg
#Assignment #4 Pacman
#Friday 9AM

import pygame
from pygame.sprite import Sprite
from spritesheet import Sheet


class Pacman(Sprite):
    def __init__(self, settings, screen):
        super(Pacman, self).__init__()
        self.dots_eaten = 0
        self.settings = settings
        self.screen = screen
        self.sheet = Sheet()
        self.image = self.sheet.image(376, 0, 38, 38)
        self.image = pygame.transform.scale(self.image, (settings.block_width, settings.block_height))
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.ticks = 0
        self.MOVINGUP = self.MOVINGDOWN = self.MOVINGLEFT = self.MOVINGRIGHT = False
        self.frame = 0
        self.move_tick = 0
        self.last_x = 0
        self.last_y = 0
        self.intent = 'none'
        self.angle = 0

    def update(self):

        self.last_x = self.rect.x
        self.last_y = self.rect.y

        current = pygame.time.get_ticks()
        if current - self.move_tick > 8:
            self.move_tick = current
            if self.MOVINGLEFT:
                self.rect.x -= 1
            elif self.MOVINGRIGHT:
                self.rect.x += 1
            elif self.MOVINGUP:
                self.rect.y -= 1
            elif self.MOVINGDOWN:
                self.rect.y += 1

        if self.rect.center == (-15, 290):
            self.rect.center = (579, 290)
        if self.rect.center == (580, 290):
            self.rect.center = (-14, 290)

    def blitme(self):
        current = pygame.time.get_ticks()
        if current - self.ticks > 80:
            self.ticks = current
            self.animate()
        self.screen.blit(self.image, self.rect)

    def animate(self):
        if self.MOVINGRIGHT:
            if self.frame == 0:
                self.image = self.sheet.image(376, 0, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 1
                return
            if self.frame == 1:
                self.image = self.sheet.image(376, 38, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 2
                return
            if self.frame == 2:
                self.image = self.sheet.image(376, 76, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 0
                return

        if self.MOVINGLEFT:
            if self.frame == 0:
                self.image = self.sheet.image(338, 0, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 1
                return
            if self.frame == 1:
                self.image = self.sheet.image(338, 38, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 2
                return
            if self.frame == 2:
                self.image = self.sheet.image(338, 76, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 0
                return

        if self.MOVINGUP:
            if self.frame == 0:
                self.image = self.sheet.image(338, 114, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 1
                return
            if self.frame == 1:
                self.image = self.sheet.image(338, 152, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 2
                return
            if self.frame == 2:
                self.image = self.sheet.image(338, 190, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 0
                return

        if self.MOVINGDOWN:
            if self.frame == 0:
                self.image = self.sheet.image(376, 114, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 1
                return
            if self.frame == 1:
                self.image = self.sheet.image(376, 152, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 2
                return
            if self.frame == 2:
                self.image = self.sheet.image(376, 190, 38, 38)
                self.image = pygame.transform.scale(self.image, (self.settings.block_width, self.settings.block_height))
                self.frame = 0
                return
