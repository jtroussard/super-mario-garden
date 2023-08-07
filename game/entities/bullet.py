from game.entities.entity import Entity
from game.settings import COLORS
from game.utils import degree_to_slope


class Bullet(Entity):
    default_width = 8
    default_height = 8

    def __init__(self, x, y, angle):
        super().__init__(
            x,
            y,
            self.default_width,
            self.default_height,
            COLORS.get("ORANGE"),
            3,
            1,
            True,
        )
        self.angle = angle

    def move(self):
        slope = degree_to_slope(self.angle)
        self.rect.y -= self.speed * slope[0]
        self.rect.x += self.speed * slope[1]
