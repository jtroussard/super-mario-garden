import pygame
from game.entities.entity import Entity
from game.settings import SCREEN_WIDTH, SCREEN_HEIGHT, COLORS
from game.utils import calculate_face_midpoint

class Hero(Entity):
    default_height = 20
    default_width = 20
    default_head_height = 120

    def __init__(self):
        super().__init__(
            ((SCREEN_WIDTH // 2) - (self.default_width // 2)),
            self.get_rendered_y_position(),
            self.default_width,
            self.default_height,
            COLORS.get("GREEN"),
            5,
            1,
            True,
        )
        self.rot = 180
        self.rot_speed = 5
        self.image_copy = self.image.copy()
        self.face_midpoint = calculate_face_midpoint(self)

    def rotate_and_update(self):
        rotated_image = pygame.transform.rotate(self.image_copy, self.rot)
        new_rect = rotated_image.get_rect(center=self.rect.center)
        self.image = rotated_image
        self.rect = new_rect
        self.face_midpoint = calculate_face_midpoint(self)

    def get_face_midpoint(self):
        return self.face_midpoint

    def move(self, direction):
        if direction == "left":
            if self.rot < 270:
                self.rot = (self.rot + self.rot_speed) % 360
                self.rotate_and_update()
        elif direction == "right":
            if self.rot > 90:
                self.rot = (self.rot - self.rot_speed) % 360
                self.rotate_and_update()
        self.rect.x = max(0, min(self.rect.x, SCREEN_WIDTH - self.rect.width))

    def get_angle(self):
        return self.rot

    def get_rendered_y_position(self):
        return SCREEN_HEIGHT - self.default_head_height

    def get_length(self):
        return self.default_height
