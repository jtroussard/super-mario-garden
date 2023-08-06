# import weakref
from game.entities.entity import Entity
from game.settings import COLORS, SCREEN_WIDTH


class Enemy(Entity):
    default_height = 30
    default_width = 30

    def __init__(self, x, y, released=False):
        super().__init__(
            x,
            y,
            self.default_width,
            self.default_height,
            COLORS.get("RED"),
            1,
            1,
            False,
        )
        self.released = released
        # Just read about weakref in python - cool - probably wont use it in
        # this game but just in case to jog my memory later
        # self._weakref = weakref.ref(self)

    def move(self):
        self.rect.y += self.speed
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
