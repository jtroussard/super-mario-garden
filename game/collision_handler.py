"""
Collision handler class.
"""
import pygame

class CollisionHandler:
    """
    Handle collisions.
    """
    def __init__(self):
        """
        Initialize the collision handler.
        """
        self.active_sprites = None
        self.active_enemies = None
        self.active_bullets = None

    def set_sprite_groups(self, active_sprites, active_enemies, active_bullets):
        """
        Set the sprite groups.
        """
        self.active_sprites = active_sprites
        self.active_enemies = active_enemies
        self.active_bullets = active_bullets

    def handle_collisions(self):
        """
        Handle collisions.
        """
        self.handle_bullet_enemy_collisions()

    def handle_bullet_enemy_collisions(self):
        """
        Handle bullet and enemy collisions.
        """
        # Have a few ways of implementation this logic, going with the double
        # for loop for now, but I am going to leave my original implementation here
        # and mess around with it later.
        # --- ORIGINAL METHOD IMPLEMENTATION ---
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
        # for active_entity in pygame.sprite.Group.sprites(self.active_sprites):
        #     if isinstance(active_entity, Bullet):
        #         if (
        #             active_entity.rect.y < 0
        #             or active_entity.rect.x < (0 - Bullet.default_width)
        #             or active_entity.rect.x + Bullet.default_width > settings.SCREEN_WIDTH
        #         ):
        #             active_entity.active = False
        #             active_entity.kill()
        #         else:
        #             contact = pygame.sprite.spritecollideany(active_entity, self.active_enemies)
        #             if contact:
        #                 active_entity.active = False
        #                 active_entity.kill()
        #                 contact.active = False
        #                 contact.kill()
        #     elif isinstance(active_entity, Enemy):
        #         if active_entity.rect.y > settings.SCREEN_HEIGHT:
        #             active_entity.active = False
        #             active_entity.kill()
        for bullet in pygame.sprite.Group.sprites(self.active_bullets):
            for enemy in pygame.sprite.spritecollide(bullet, self.active_enemies, True):
                bullet.active = False
                bullet.kill()
                enemy.active = False
                enemy.kill()
