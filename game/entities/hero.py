import pygame
from game.entities.entity import Entity
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS

default_height = 20
default_width = 70
default_head_height = 120

class Hero(Entity):
    def __init__(self):
        super().__init__(
            ((SCREEN_WIDTH // 2) - (default_width // 2)),
            SCREEN_HEIGHT - default_head_height,
            default_width,
            default_height,
            COLORS.get("GREEN"),
            5,
            1,
            True,
        )
        self.rot = 180
        self.rot_speed = 5
        self.image_copy = self.image.copy()

    def rotate_and_update(self):
        rotated_image = pygame.transform.rotate(self.image_copy, self.rot)
        self.image = rotated_image
        self.rect = rotated_image.get_rect(center=self.rect.center)

    def move(self, direction):
        if direction == "left":
            if self.rot < 270:
                self.rot = (self.rot + self.rot_speed) % 360
                self.rotate_and_update()
                print(f"rot: {self.rot} rot_speed: {self.rot_speed} direction: {direction}")
            else:
                print("MAXIMUM LEFT ROTATION REACHED")
        elif direction == "right":
            if self.rot > 90:
                self.rot = (self.rot - self.rot_speed) % 360
                self.rotate_and_update()
                print(f"rot: {self.rot} rot_speed: {self.rot_speed} direction: {direction}")
            else:
                print("MAXIMUM RIGHT ROTATION REACHED")

        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))
