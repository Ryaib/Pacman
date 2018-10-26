#Paul Lindberg
#Assignment #4 Pacman
#Friday 9AM

import pygame


class Settings:
    def __init__(self):
        self.HEIGHT = 560
        self.WIDTH = 620
        self.BLACK = (0, 0, 0)
        self.block_width = self.block_height = 20
        self.myfont = pygame.font.SysFont(None, 30)
        self.menufont = pygame.font.SysFont(None, 60)
        self.first_run = True
        self.waka = True
        self.GAME_ACTIVE = False
        self.title = pygame.image.load('title.PNG')
        self.num_scores = 0
