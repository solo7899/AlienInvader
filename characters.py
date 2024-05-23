import random
import pygame
from pygame.locals import (
    K_LEFT,
    K_RIGHT
)

class Player(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDHT:  int, SCREEN_HEIGHT: int) -> None:
        super(Player, self).__init__()
        self.surf = pygame.Surface((40, 10))        
        self.surf.fill("BLACK")
        self.rect = self.surf.get_rect(
            center = (SCREEN_WIDHT/2, SCREEN_HEIGHT-10), )
        self.SCREEN_WIDTH = SCREEN_WIDHT
    
    def update(self, keys_pressed: pygame.key.ScancodeWrapper):
        if keys_pressed[K_RIGHT]:
            self.rect.move_ip(+5, 0)
        elif keys_pressed[K_LEFT]:
            self.rect.move_ip(-5, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > self.SCREEN_WIDTH:
            self.rect.right = self.SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
    def __init__(self, SCREEN_WIDTH: int) -> None:
        super(Enemy, self).__init__()
        self.surf = pygame.Surface((20, 20))
        self.surf.fill("PURPLE")
        self.rect = self.surf.get_rect(
            center = (random.randint(20, SCREEN_WIDTH-20), random.randint(10, 100))
        )
        self.SCREEN_WIDTH = SCREEN_WIDTH
        self.movement = random.choice([1, -1, -2, 2])

    def update(self):
        if self.rect.left < 0 or self.rect.right > self.SCREEN_WIDTH:
            self.movement *= -1
        self.rect.move_ip(2 * self.movement, 0)


class Bullet(pygame.sprite.Sprite):
    def __init__(self, SCREEN_HEIGHT: int, playerMid: tuple[int, int]) -> None:
        super(Bullet, self).__init__()
        self.surf = pygame.Surface((2, 5))
        self.surf.fill("BLACK")
        self.rect = self.surf.get_rect(
            center = playerMid,
        )
        self.SCREEN_HEIGHT = SCREEN_HEIGHT

    def update(self) -> None:
        self.rect.move_ip(0, -5)

        if self.rect.bottom < 0:
            self.kill()

class PlayerBullet(Bullet):
    def __init__(self, SCREEN_HEIGHT: int, playerMid: tuple[int, int]) -> None:
        super(PlayerBullet, self).__init__(SCREEN_HEIGHT, playerMid)

class EnemyBullet(Bullet):
    def __init__(self, SCREEN_HEIGHT: int, enemyMid: tuple[int, int]) -> None:
        super(EnemyBullet, self).__init__(SCREEN_HEIGHT, enemyMid)
        self.surf.fill("PURPLE")
        
    def update(self) -> None:
        self.rect.move_ip(0, 5)
        
        if self.rect.top > self.SCREEN_HEIGHT:
            self.kill()