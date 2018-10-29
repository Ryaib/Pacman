# Paul Lindberg
# Assignment 4 Pacman
# Friday 9AM

import pygame
from pygame.sprite import Sprite


class Portal(Sprite):
    def __init__(self, screen):
        super(Portal, self).__init__()
        self.screen = screen
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.portal_viable = True
        self.blue_active = False
        self.orange_active = False
        self.blue_rect = pygame.Rect(0, 0, 20, 20)
        self.orange_rect = pygame.Rect(0, 0, 20, 20)
        self.tele = False
        self.ticks = 0

    def update(self, pacman):

        if self.tele:
            current = pygame.time.get_ticks()
            if current - self.ticks > 500:
                self.tele = False

        if pacman.MOVINGRIGHT:
            self.rect.x = pacman.rect.x
            self.rect.x += 20
            self.rect.y = pacman.rect.y
            return
        if pacman.MOVINGLEFT:
            self.rect.x = pacman.rect.x
            self.rect.x -= 20
            self.rect.y = pacman.rect.y
            return
        if pacman.MOVINGDOWN:
            self.rect.x = pacman.rect.x
            self.rect.y = pacman.rect.y
            self.rect.y += 20
            return
        if pacman.MOVINGUP:
            self.rect.x = pacman.rect.x
            self.rect.y = pacman.rect.y
            self.rect.y -= 20
            return

    def blue_portal(self):
        if self.portal_viable:
            self.blue_active = True

            localx = self.rect.centerx
            localy = self.rect.centery
            int(localx)
            int(localy)
            print(localx, localy)
            self.blue_rect.centerx = localx
            self.blue_rect.centery = localy
            return

    def orange_portal(self):
        if self.portal_viable:
            self.orange_active = True
            localx = self.rect.centerx
            localy = self.rect.centery
            int(localx)
            int(localy)
            print(localx, localy)
            self.orange_rect.centerx = localx
            self.orange_rect.centery = localy
            return

    def draw(self):
        if self.blue_active:
            pygame.draw.circle(self.screen, (0, 227, 252), (self.blue_rect.centerx, self.blue_rect.centery), 10)
        if self.orange_active:
            pygame.draw.circle(self.screen, (252, 193, 0), (self.orange_rect.centerx, self.orange_rect.centery), 10)
        return
