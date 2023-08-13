# import weakref
from game.entities.entity import Entity
from game.settings import COLORS


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
    
    def __repr__(self) -> str:
        return f"Enemy\n\tposition:({self.rect.x}, {self.rect.y})\n\
            speed: {self.speed}\n------"
