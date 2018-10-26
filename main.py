#Paul Lindberg
#Assignment #4 Pacman
#Friday 9AM

import pygame
from settings import Settings
from pygame.sprite import Group
import game_functions as gf
from Pacman import Pacman
from Score import Score
import sys
from Ghost import Ghost


def open_file(settings):
    f = open('scores.txt', "r")
    data = f.readlines()
    for x in data:
        settings.num_scores += 1
        print(x)
    f.close()

    return data


def run_game():
    pygame.init()
    pygame.font.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.HEIGHT, settings.WIDTH))
    pygame.display.set_caption("Pacman")
    blocks = Group()
    dots = Group()
    powers = Group()
    nodes = Group()
    pacman = Pacman(settings, screen)
    score = Score(settings, screen)
    menupac = Pacman(settings, screen)
    blinky = Ghost(screen, 'Blinky', (150, 200), settings)
    inky = Ghost(screen, 'Inky', (150, 250), settings)
    pinky = Ghost(screen, 'Pinky', (150, 300), settings)
    clyde = Ghost(screen, 'Clyde', (150, 350), settings)
    listed = open_file(settings)
    title = settings.title

    while not settings.GAME_ACTIVE:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                settings.GAME_ACTIVE = True
        textsurface = settings.myfont.render("PACMAN", False, (255, 255, 0))
        menupac.rect.center = (150, 150)
        menupac.MOVINGRIGHT = True
        menupac.blitme()
        screen.blit(textsurface, (180, 145))
        textsurface = settings.myfont.render("Press any Key to Continue", False, (255, 255, 255))
        screen.blit(textsurface, (150, 600))
        blinky.blitme()
        inky.blitme()
        pinky.blitme()
        clyde.blitme()
        textsurface = settings.myfont.render("BLINKY", False, (255, 0, 0))
        screen.blit(textsurface, (180, 200))
        textsurface = settings.myfont.render("INKY", False, (7, 225, 225))
        screen.blit(textsurface, (180, 250))
        textsurface = settings.myfont.render("PINKY", False, (225, 207, 231))
        screen.blit(textsurface, (180, 300))
        textsurface = settings.myfont.render("CLYDE", False, (255, 159, 7))
        screen.blit(textsurface, (180, 350))
        screen.blit(title, (0, 0))
        textsurface = settings.myfont.render("HIGH SCORES", False, (255, 255, 255))
        screen.blit(textsurface, (350, 100))
        y = 150
        for x in listed:
            if y > 550:
                break
            textsurface = settings.myfont.render(x, False, (255, 255, 255))
            screen.blit(textsurface, (450, y))
            y += 50
        pygame.display.flip()

    gf.create_maze(settings, blocks, screen, dots, pacman, powers, nodes)

    while True:
        pacman.update()
        gf.check_events(pacman, dots, blocks, powers, score, settings, screen, nodes)
        gf.update_screen(blocks, dots, pacman, screen, settings, powers, score)


run_game()
