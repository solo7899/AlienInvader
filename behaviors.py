import pygame
from pygame.locals import K_p, KEYDOWN, QUIT, K_ESCAPE
def pause(running: bool):
    is_pause: bool = True
    while is_pause:
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_p:
                    is_pause = False
                if event.key == K_ESCAPE:
                    running = False
                    is_pause = False
            if event.type == QUIT:
                running = False
                is_pause = False
    return running