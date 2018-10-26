#Paul Lindberg
#Assignment #4 Pacman
#Friday 9AM

import pygame
from pygame.sprite import Sprite


class Dot(Sprite):
    def __init__(self, x, y, settings, screen):
        super(Dot, self).__init__()
        self.settings = settings
        self.screen = screen
        self.rect = pygame.Rect(x, y, self.settings.block_width, self.settings.block_height)
        self.color = (255, 255, 255)
        self.radius = 3

    def draw_dot(self):
        pygame.draw.circle(self.screen, self.color, (self.rect.centerx, self.rect.centery), self.radius)


class Power(Sprite):
    def __init__(self, x, y, settings, screen):
        super(Power, self).__init__()
        self.settings = settings
        self.screen = screen
        self.rect = pygame.Rect(x, y, self.settings.block_width, self.settings.block_height)
        self.color = (255, 255, 255)
        self.radius = 8
        self.ticks = 0

    def draw_dot(self):
        pygame.draw.circle(self.screen, self.color, (self.rect.centerx, self.rect.centery), self.radius)
