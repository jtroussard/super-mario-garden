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

hero = Hero()
all_sprites.add(hero)
active_sprites.add(hero)

font = pygame.font.Font(None, 36)  # You can customize the font and size

clock = pygame.time.Clock()

last_enemy_release_time = 0
# Game loop
running = True
while running:
    current_time = pygame.time.get_ticks()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bullet = Bullet(hero.rect.centerx, hero.rect.top)
                all_sprites.add(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.move("left")
    if keys[pygame.K_RIGHT]:
        hero.move("right")
    if keys[pygame.K_SPACE]:
        pass

    for active_entity in [
        entity
        for entity in pygame.sprite.Group.sprites(active_sprites)
        if not isinstance(entity, Hero)
    ]:
        # Check for off board, prepare objects for garbage collection
        # Second thought, is active attribute unnecessary? with separate groups
        # for active entities?
        if isinstance(active_entity, Bullet):
            if active_entity.rect.y < 0:
                active_entity.active = False
                all_sprites.remove(active_entity)
                active_sprites.remove(active_entity)
        if isinstance(active_entity, Enemy):
            if active_entity.rect.y > settings.SCREEN_HEIGHT:
                active_entity.active = False
                all_sprites.remove(active_entity)
                active_sprites.remove(active_entity)
        # Move active entity
        active_entity.move()

    # Release enemies
    active_enemies = [enemy for entity in active_sprites if isinstance(entity, Enemy)]
    if current_time - last_enemy_release_time >= 3000:
        if len(active_enemies) < settings.MAX_ACTIVE_ENEMY_COUNT:
            enemy = Enemy(
                random.randint(0, settings.SCREEN_WIDTH - 30), Enemy.default_height
            )
            all_sprites.add(enemy)
            active_sprites.add(enemy)
            last_enemy_release_time = current_time
        else:
            print("Max active enemies reached")

    # DEBUGGING MESSAGES
    # make this a dev util - pass the target variable to print, return the font
    # render object and then make it passable into a another util that organizes
    # the messages on the screen
    time_text = font.render(f"Time: {current_time}", True, (255, 255, 255))
    active_enemies_text = font.render(
        f"Active enemies vs. All: {len(active_enemies)}/{len(pygame.sprite.Group.sprites(all_sprites))}",
        True,
        (255, 255, 255),
    )
    release_timer_text = font.render(
        f"Release timer: {current_time - last_enemy_release_time}",
        True,
        (255, 255, 255),
    )

    # Update
    all_sprites.update()

    # Draw
    screen.fill(settings.COLORS.get("BLACK"))
    active_sprites.draw(screen)
    screen.blit(time_text, (10, 10))
    screen.blit(active_enemies_text, (10, 40))
    screen.blit(release_timer_text, (10, 70))

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
