#! /home/kali/programming/pythoning/alienInvader/.venv/bin/python3

import pygame
from pygame.locals import (
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE
)
import pygame.sprite


from characters import Player, Enemy, Bullet

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGH = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))

    clock = pygame.time.Clock()

    SPAWN_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ENEMY, 500)
    
    all_sprites = pygame.sprite.Group()
    enemies = pygame.sprite.Group()
    bullets = pygame.sprite.Group()
    
    player = Player(SCREEN_WIDTH, SCREEN_HEIGH)
    all_sprites.add(player)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                if event.key == K_SPACE:
                    bullet = Bullet(SCREEN_HEIGH, player.rect.midbottom)
                    bullets.add(bullet)
                    all_sprites.add(bullet)
            if event.type == SPAWN_ENEMY:
                enemy = Enemy(SCREEN_WIDTH)
                enemies.add(enemy)
                all_sprites.add(enemy)
                    
        player.update(pygame.key.get_pressed())

        bullets.update()
        enemies.update()

        screen.fill((255, 255, 255))

        for sprite in all_sprites:
            screen.blit(sprite.surf, sprite.rect)

        pygame.sprite.groupcollide(bullets, enemies, True, True)
        pygame.display.flip()

        clock.tick(60)
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()