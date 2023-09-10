import sys
import random
import pygame
import json
from . import settings
from game.entities.hero import Hero
from game.entities.enemy import Enemy
from game.entities.bullet import Bullet
from game.collision_handler import CollisionHandler
from game.debug_drawer import DebugDrawer

class Game:
    def __init__(self, dev_mode=False):
        """
        Initialize the game, set up the screen, and load assets. Defaults to production mode.
        """
        pygame.init()
        self.dev_mode = dev_mode
        self.font = pygame.font.Font(None, 36)

        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        pygame.display.set_caption(f"Super Mario Garden v{settings.VERSION}")

        self.clock = pygame.time.Clock()
        self.collision_handler = CollisionHandler()
        self.draw_debug = DebugDrawer()

        self.setup_environment()
        self.init_entities()

        # These are more development variables, will organize or remove later
        self.last_enemy_release_time = 0 # game mechanics, should organize elsewhere
    
    def setup_environment(self):
        """
        Set up the game environment based on the mode. Defaults to production mode.
        """
        if self.dev_mode:
            print("Setting up dev environment")
            # block assets, no noises, etc.
        elif self.prod_mode:
            print("Setting up prod environment")
            # you can do something like load real assets here
        else:
            print("No environment set") # Not sure what action to take here. Maybe a retry or define a default mode?

    def init_entities(self):
        """
        Initialize the game entities.
        """

        self.all_sprites = pygame.sprite.Group()
        self.active_sprites = pygame.sprite.Group()
        self.active_enemies = pygame.sprite.Group()
        self.active_bullets = pygame.sprite.Group()

        self.hero = Hero()
        self.all_sprites.add(self.hero)
        self.active_sprites.add(self.hero)  # For drawing and updating... I think

    def run(self):
        running = True
        while running:
            self.current_time = pygame.time.get_ticks()
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if (
                        len(pygame.sprite.Group.sprites(self.active_bullets))
                        >= settings.MAX_ACTIVE_BULLET_COUNT
                    ):
                        # TODO: Replace this logic/conditional with the weapon class
                        print("Max active bullets reached")
                    else:
                        fire_coords = self.hero.get_face_midpoint()
                        bullet = Bullet(
                            fire_coords[0] - Bullet.default_width / 2,
                            fire_coords[1] - Bullet.default_height,
                            self.hero.get_angle(),
                        )
                        print(f"fire_coords: {fire_coords}")
                        self.all_sprites.add(bullet)
                        self.active_sprites.add(bullet)
                        self.active_bullets.add(bullet)
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.hero.move("left")
        if keys[pygame.K_RIGHT]:
            self.hero.move("right")

    def update(self):
        self.move_bullets_and_enemies()
        self.handle_collisions()
        self.release_enemies()

    def move_bullets_and_enemies(self):
        for active_entity in pygame.sprite.Group.sprites(self.active_sprites):
            if not isinstance(active_entity, Hero):
                active_entity.move()

    def release_enemies(self):
        self.active_enemies = [entity for entity in self.active_sprites if isinstance(entity, Enemy)]
        if self.current_time - self.last_enemy_release_time >= 3000:
            if len(self.active_enemies) < settings.MAX_ACTIVE_ENEMY_COUNT:
                enemy = Enemy(
                    random.randint(0, settings.SCREEN_WIDTH - 30), Enemy.default_height
                )
                self.all_sprites.add(enemy)
                self.active_sprites.add(enemy)
                self.last_enemy_release_time = self.current_time
            else:
                print("Max active enemies reached")

    def draw(self):
        self.screen.fill(settings.COLORS.get("BLACK"))  # Clear the screen - Don't Move Me!

        if self.dev_mode:
            self.draw_debug_mode()  # Draw debugging elements

        self.active_sprites.draw(self.screen)  # Draw game entities
        pygame.display.flip()  # Update the display

    

if __name__ == "__main__":
    game = Game()
    game.run()
