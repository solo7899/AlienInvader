#! /home/kali/programming/pythoning/alienInvader/.venv/bin/python3

import random
import pygame
from pygame.locals import (
    QUIT,
    K_ESCAPE,
    KEYDOWN,
    K_SPACE
)
import pygame.sprite


from characters import Player, Enemy, PlayerBullet, EnemyBullet

def main():
    pygame.init()

    SCREEN_WIDTH = 800
    SCREEN_HEIGH = 600

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGH))

    clock = pygame.time.Clock()

    SPAWN_ENEMY = pygame.USEREVENT + 1
    pygame.time.set_timer(SPAWN_ENEMY, 500)

    ENEMY_SHOOT = pygame.USEREVENT + 2
    pygame.time.set_timer(ENEMY_SHOOT, 750)
    
    all_sprites = pygame.sprite.Group()
    enemies: list[Enemy] = pygame.sprite.Group()
    bullets: list[PlayerBullet] = pygame.sprite.Group()
    enemiesBullets: list[EnemyBullet] = pygame.sprite.Group()
    
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
                    bullet = PlayerBullet(SCREEN_HEIGH, player.rect.midbottom)
                    bullets.add(bullet)
                    all_sprites.add(bullet)
            if event.type == SPAWN_ENEMY:
                enemy = Enemy(SCREEN_WIDTH)
                enemies.add(enemy)
                all_sprites.add(enemy)
            if event.type == ENEMY_SHOOT:
                for enemy in enemies: 
                    permitted: bool = random.choice([True, False])
                    if permitted:
                        bullet = EnemyBullet(SCREEN_HEIGH, enemy.rect.midtop)
                        enemiesBullets.add(bullet)
                        all_sprites.add(bullet)
                    
        player.update(pygame.key.get_pressed())

        bullets.update()
        enemies.update()
        enemiesBullets.update()

        screen.fill((255, 255, 255))

        for sprite in all_sprites:
            screen.blit(sprite.surf, sprite.rect)

        pygame.sprite.groupcollide(bullets, enemies, True, True)

        if pygame.sprite.spritecollideany(player, enemiesBullets):
            running = False
            print("got hit")
            player.kill()
            
        pygame.display.flip()

        clock.tick(60)
        
    pygame.quit()
    
    
if __name__ == "__main__":
    main()