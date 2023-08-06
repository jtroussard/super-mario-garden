from game.entities.entity import Entity
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS


class Hero(Entity):
    def __init__(self):
        super().__init__(
            SCREEN_WIDTH // 2,
            SCREEN_HEIGHT - 50,
            50,
            30,
            COLORS.get("GREEN"),
            5,
            1,
            True,
        )

    def move(self, direction):
        if direction == "left":
            self.rect.x -= self.speed
        elif direction == "right":
            self.rect.x += self.speed

        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
