import pygame

# not even sure I want to do it this way, but I am going to leave this here if doing this manually causes issues.
class ActiveSpriteGroup(pygame.sprite.Group):
    def draw_active(self, surface):
        active_sprites = [sprite for sprite in self.sprites() if sprite.active]
        super().draw(surface, active_sprites)

def create_sprite_group():
    return ActiveSpriteGroup()

# When I get to it, I need to put collision shit in here.