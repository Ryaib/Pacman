import pygame
from pygame.sprite import Sprite


class Block(Sprite):
    def __init__(self, x, y, settings, screen):
        super(Block, self).__init__()
        self.settings = settings
        self.screen = screen
        self.rect = pygame.Rect(x, y, self.settings.block_width, self.settings.block_height)
        self.color = (0, 0, 255)

    def draw_square(self):
        pygame.draw.rect(self.screen, self.color, self.rect)
