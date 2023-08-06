import pygame
import sys
import random

from game.entities.hero import Hero
from game.entities.enemy import Enemy
from game.entities.bullet import Bullet

from . import levels
from . import settings
from . import utils


pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(f"Super Mario Garden v{settings.VERSION}")


all_sprites = pygame.sprite.Group()
active_sprites = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bullets = pygame.sprite.Group()

hero = Hero()
all_sprites.add(hero)
active_sprites.add(hero)

for _ in range(settings.ENEMY_COUNT):
    enemy = Enemy(random.randint(0, settings.SCREEN_WIDTH - 30), Enemy.default_height)
    all_sprites.add(enemy)
    enemies.add(enemy)

font = pygame.font.Font(None, 36)  # You can customize the font and size

clock = pygame.time.Clock()

# Game loop
running = True
last_enemy_release_time = 0 # This should be a variable called release rate, link to level module
last_enemy_selected = None
total_released = 0
while running:
    enemies_released = 0
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(hero.rect.centerx, hero.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.move("left")
    if keys[pygame.K_RIGHT]:
        hero.move("right")
    if keys[pygame.K_SPACE]:
        pass

    for bullet in bullets:
        bullet.move()

    # Release enemies
    active_enemies = [enemy for enemy in enemies if enemy.active]
    if current_time - last_enemy_release_time >= 3000:
        if len(active_enemies) < settings.ENEMY_ACTIVE_COUNT:
            unreleased_enemies = [enemy for enemy in pygame.sprite.Group.sprites(enemies) if not enemy.released]
            enemy = random.choice(unreleased_enemies)
            enemy.active = True
            active_sprites.add(enemy)
            enemies_released += 1
            last_enemy_release_time = current_time
            last_enemy_selected = enemy
            total_released += 1
    for enemy in active_enemies:
        if enemy.rect.y >= settings.SCREEN_HEIGHT:
            enemy.active = False
            active_sprites.remove(enemy)
        enemy.move()

    # Print current time
    time_text = font.render(f"Time: {current_time}", True, (255, 255, 255))
    active_enemies_text = font.render(f"Active enemies: {len(active_enemies)}", True, (255, 255, 255))
    release_conditional_text = font.render(f"Active vs MAX: {len(active_enemies) < settings.ENEMY_ACTIVE_COUNT}", True, (255, 255, 255))
    active_sprites_text = font.render(f"Active sprites: {len(active_sprites)}", True, (255, 255, 255))  
    enemies_group_text = font.render(f"Enemies group: {len(enemies)}", True, (255, 255, 255))
    enemies_released_text = font.render(f"Enemies released: {enemies_released}", True, (255, 255, 255)) 
    total_released_text = font.render(f"Total released: {total_released}", True, (255, 255, 255))

    # Update
    all_sprites.update()

    # Draw
    screen.fill(settings.COLORS.get('BLACK'))
    active_sprites.draw(screen)
    screen.blit(time_text, (10, 10))
    screen.blit(active_enemies_text, (10, 40))
    screen.blit(release_conditional_text, (10, 70))
    screen.blit(active_sprites_text, (10, 100))
    screen.blit(enemies_group_text, (10, 130))
    screen.blit(enemies_released_text, (10, 160))
    screen.blit(total_released_text, (10, 190))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
