import sys
import random
import pygame

from game.entities.hero import Hero
from game.entities.enemy import Enemy
from game.entities.bullet import Bullet

# from . import levels
# from . import utils
from . import settings

pygame.init()

screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
pygame.display.set_caption(f"Super Mario Garden v{settings.VERSION}")


all_sprites = pygame.sprite.Group()
active_sprites = pygame.sprite.Group()
active_enemies = pygame.sprite.Group()
active_bullets = pygame.sprite.Group()


hero = Hero()
all_sprites.add(hero)
active_sprites.add(hero)  # For drawing and updating... I think

font = pygame.font.Font(None, 36)  # Development mode only

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
                if (
                    len(pygame.sprite.Group.sprites(active_bullets))
                    >= settings.MAX_ACTIVE_BULLET_COUNT
                ):
                    # TODO: Replace this logic/conditional with the weapon class
                    print("Max active bullets reached")
                else:
                    fire_coords = hero.get_face_midpoint()
                    bullet = Bullet(
                        fire_coords[0] - Bullet.default_width / 2,
                        fire_coords[1] - Bullet.default_height,
                        hero.get_angle(),
                    )
                    print(f"fire_coords: {fire_coords}")
                    all_sprites.add(bullet)
                    active_sprites.add(bullet)
                    active_bullets.add(bullet)

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        hero.move("left")
    if keys[pygame.K_RIGHT]:
        hero.move("right")
    if keys[pygame.K_SPACE]:
        pass

    # MOVE BULLETS AND ENEMIES
    for active_entity in pygame.sprite.Group.sprites(active_sprites):
        if not isinstance(active_entity, Hero):
            active_entity.move()

    # Check for off board, prepare objects for garbage collection
    # Second thought, is active attribute unnecessary? with separate groups
    # for active entities? UPDATE 99% sure it is not necessary, using the kill()
    # method here, and will open an issue/branch to come back and remove the 'active'
    # attribute concept from the entity class.
    # ---
    # For now the out of bounds detection is being split up by entity type
    # because they move in opposite directions, but I have a good feeling the
    # logic could be combined and moved into the parent class. Need to think
    # about the edge cases. TBD.
    # CHECK FOR OUT OF BOUNDS AND COLLISIONS IN THAT ORDER
    for active_entity in pygame.sprite.Group.sprites(active_sprites):
        if isinstance(active_entity, Bullet):
            if (
                active_entity.rect.y < 0
                or active_entity.rect.x < (0 - Bullet.default_width)
                or active_entity.rect.x + Bullet.default_width > settings.SCREEN_WIDTH
            ):
                active_entity.active = False
                active_entity.kill()
            else:
                contact = pygame.sprite.spritecollideany(active_entity, active_enemies)
                if contact:
                    active_entity.active = False
                    active_entity.kill()
                    contact.active = False
                    contact.kill()
        elif isinstance(active_entity, Enemy):
            if active_entity.rect.y > settings.SCREEN_HEIGHT:
                active_entity.active = False
                active_entity.kill()

    # RELEASE ENEMIES
    active_enemies = [entity for entity in active_sprites if isinstance(entity, Enemy)]
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
        f"Active enemies vs. All:\
            {len(active_enemies)}/{len(pygame.sprite.Group.sprites(all_sprites))}",
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
    screen.fill(settings.COLORS.get("BLACK"))  # Don't move me

    # Development Stage Grids
    center_x = settings.SCREEN_WIDTH // 2
    center_y = settings.SCREEN_HEIGHT // 2
    pygame.draw.line(
        screen,
        (settings.COLORS.get("WHITE")),
        (center_x, 0),
        (hero.rect.x + (hero.default_width / 2), hero.rect.y + 50),
    )
    pygame.draw.line(
        screen,
        (settings.COLORS.get("BLUE")),
        (0, settings.SCREEN_HEIGHT // 2),
        (settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT // 2),
    )

    active_sprites.draw(screen)
    screen.blit(time_text, (10, 10))
    screen.blit(active_enemies_text, (10, 40))
    screen.blit(release_timer_text, (10, 70))

    # Draw a small circle on the hero.rect.top to show the center face of the hero
    pygame.draw.circle(
        screen,
        (settings.COLORS.get("PURPLE")),
        (hero.get_face_midpoint()),
        5,
        5,
        True,
        True,
        True,
        True,
    )

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
