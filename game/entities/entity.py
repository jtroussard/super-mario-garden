# pylint: disable=too-many-arguments
import pygame


# disabling too-many-arguments for now - if this gets out of hand maybe think of a refactor
# e.g. group parameters into their special dicts/objects
class Entity(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, color, speed, life, active):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
        self.color = color
        self.life = life
        self.active = active
