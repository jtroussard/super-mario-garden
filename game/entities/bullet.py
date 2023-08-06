from game.entities.entity import Entity
from game.settings import COLORS


class Bullet(Entity):
    def __init__(self, x, y):
        super().__init__(x, y, 5, 5, COLORS.get('BLUE'), 8, 1)

    def move(self):
        self.rect.y -= self.speed