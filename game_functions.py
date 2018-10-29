# Paul Lindberg
# Assignment 4 Pacman
# Friday 9AM

import sys
import pygame
from maze import Maze
from Block import Block
from dots import Dot
from dots import Power
from node import Node


def check_events(pacman, dots, blocks, powers, score, settings, screen, nodes, portal):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, pacman, portal)
    check_colissions(pacman, dots, blocks, powers, score, settings, screen, nodes, portal)


def dot_sound(settings):
    if settings.waka:
        pygame.mixer.Channel(0).play(pygame.mixer.Sound('sounds/waka1.wav'))
        settings.waka = False
        return
    if not settings.waka:
        pygame.mixer.Channel(1).play(pygame.mixer.Sound('sounds/waka2.wav'))
        settings.waka = True
        return


def collide_func(pacman, blocks):
    block_collide = pygame.sprite.spritecollide(pacman, blocks, False)
    if block_collide:
        pacman.rect.x = pacman.last_x
        pacman.rect.y = pacman.last_y
        return True
    return False


def check_colissions(pacman, dots, blocks, powers, score, settings, screen, nodes, portal):
    block_collide = pygame.sprite.spritecollide(pacman, blocks, False)
    points = pygame.sprite.spritecollide(pacman, dots, True)
    pygame.sprite.spritecollide(pacman, powers, True)
    portal_space = pygame.sprite.spritecollide(portal, blocks, False)

    if pacman.rect.centerx == portal.blue_rect.centerx and pacman.rect.centery == portal.blue_rect.centery and portal.orange_active\
            and not portal.tele:
        localx = portal.orange_rect.centerx
        localy = portal.orange_rect.centery
        int(localx)
        int(localy)
        pacman.rect.centerx = localx
        pacman.rect.centery = localy
        portal.tele = True
        portal.ticks = pygame.time.get_ticks()
    if pacman.rect.centerx == portal.orange_rect.centerx and pacman.rect.centery == portal.orange_rect.centery and portal.blue_active\
            and not portal.tele:
        localx = portal.blue_rect.centerx
        localy = portal.blue_rect.centery
        int(localx)
        int(localy)
        pacman.rect.centerx = localx
        pacman.rect.centery = localy
        portal.tele = True
        portal.ticks = pygame.time.get_ticks()

    if portal_space:
        portal.portal_viable = False
    elif not portal_space:
        portal.portal_viable = True

    if block_collide:
        pacman.rect.x = pacman.last_x
        pacman.rect.y = pacman.last_y
        pacman.MOVINGLEFT = pacman.MOVINGDOWN = pacman.MOVINGUP = pacman.MOVINGRIGHT = False
        pacman.intent = 'none'

    if points:
        score.value += 10
        pacman.dots_eaten += 1
        dot_sound(settings)
        if pacman.dots_eaten == 244:
            reset_level(pacman, settings, dots, powers, screen)

    for node in nodes.sprites():
        if pacman.rect.center == node.rect.center:

            if pacman.intent == 'up':
                pacman.MOVINGDOWN = pacman.MOVINGLEFT = pacman.MOVINGRIGHT = False
                pacman.MOVINGUP = True
                pacman.intent = 'none'

            elif pacman.intent == 'down':
                pacman.MOVINGUP = pacman.MOVINGLEFT = pacman.MOVINGRIGHT = False
                pacman.MOVINGDOWN = True
                pacman.intent = 'none'

            elif pacman.intent == 'left':
                pacman.MOVINGRIGHT = pacman.MOVINGUP = pacman.MOVINGDOWN = False
                pacman.MOVINGLEFT = True
                pacman.intent = 'none'

            elif pacman.intent == 'right':
                pacman.MOVINGLEFT = pacman.MOVINGUP = pacman.MOVINGDOWN = False
                pacman.MOVINGRIGHT = True
                pacman.intent = 'none'


def reset_level(pacman, settings, dots, powers, screen):
    pacman.dots_eaten = 0
    maze = Maze(settings)
    divx = 0
    divy = 0

    for x in maze.list:
        if x == 'X':
            divx += settings.block_width

        elif x == '\n':
            divx = 0
            divy += settings.block_height
        elif x == '.':
            dot = Dot(divx, divy, settings, screen)
            dots.add(dot)
            divx += settings.block_width
        elif x == 'P':
            pacman.rect.x = divx
            pacman.rect.y = divy
            divx += settings.block_width
        elif x == 'O':
            power = Power(divx, divy, settings, screen)
            power.add(powers)
            divx += settings.block_width
        elif x == 'I':
            dot = Dot(divx, divy, settings, screen)
            dots.add(dot)
            divx += settings.block_width
        elif x == 'Q':
            power = Power(divx, divy, settings, screen)
            power.add(powers)
            divx += settings.block_width

        else:
            divx += settings.block_width


def check_keydown_events(event, pacman, portal):
    if event.key == pygame.K_RIGHT:
        if pacman.MOVINGUP or pacman.MOVINGDOWN:
            pacman.intent = 'right'
        else:
            pacman.MOVINGRIGHT = True
            pacman.MOVINGLEFT = False
    elif event.key == pygame.K_LEFT:
        if pacman.MOVINGUP or pacman.MOVINGDOWN:
            pacman.intent = 'left'
        else:
            pacman.MOVINGRIGHT = False
            pacman.MOVINGLEFT = True
    elif event.key == pygame.K_UP:
        if pacman.MOVINGLEFT or pacman.MOVINGRIGHT:
            pacman.intent = 'up'
        else:
            pacman.MOVINGUP = True
            pacman.MOVINGDOWN = False
    elif event.key == pygame.K_DOWN:
        if pacman.MOVINGLEFT or pacman.MOVINGRIGHT:
            pacman.intent = 'down'
        else:
            pacman.MOVINGUP = False
            pacman.MOVINGDOWN = True
    elif event.key == pygame.K_q:
        portal.blue_portal()
    elif event.key == pygame.K_e:
        portal.orange_portal()


def update_screen(blocks, dots, pacman, screen, settings, powers, score, portal):
    screen.fill(settings.BLACK)

    for block in blocks.sprites():
        block.draw_square()
    pacman.blitme()
    for dot in dots.sprites():
        dot.draw_dot()
    for power in powers.sprites():
        power.draw_dot()
    score.blitme()
    portal.draw()
    pygame.display.flip()
    if settings.first_run:
        pygame.time.wait(4500)
        settings.first_run = False


def create_maze(settings, blocks, screen, dots, pacman, powers, nodes):
    pygame.mixer.music.load('sounds/start.wav')
    pygame.mixer.music.play(0)
    pacman.dots_eaten = 0
    maze = Maze(settings)
    divx = 0
    divy = 0

    for x in maze.list:
        if x == 'X':
            block = Block(divx, divy, settings, screen)
            blocks.add(block)
            divx += settings.block_width

        elif x == '\n':
            divx = 0
            divy += settings.block_height
        elif x == '.':
            dot = Dot(divx, divy, settings, screen)
            dots.add(dot)
            divx += settings.block_width
        elif x == 'P':
            pacman.rect.x = divx
            pacman.rect.y = divy
            divx += settings.block_width
        elif x == 'O':
            power = Power(divx, divy, settings, screen)
            power.add(powers)
            divx += settings.block_width
        elif x == 'I':
            node = Node(divx, divy, settings, screen)
            nodes.add(node)
            dot = Dot(divx, divy, settings, screen)
            dots.add(dot)
            divx += settings.block_width

        elif x == 'Q':
            node = Node(divx, divy, settings, screen)
            nodes.add(node)
            power = Power(divx, divy, settings, screen)
            power.add(powers)
            divx += settings.block_width
        elif x == 'i':
            node = Node(divx, divy, settings, screen)
            nodes.add(node)
            divx += settings.block_width

        else:
            divx += settings.block_width
