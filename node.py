from pygame.sprite import Sprite
import pygame


class Node(Sprite):
    def __init__(self, divx, divy, settings, screen):
        super(Node, self).__init__()
        self.settings = settings
        self.screen = screen
        self.rect = pygame.Rect(divx, divy, self.settings.block_width, self.settings.block_height)

