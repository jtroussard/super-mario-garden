import pygame
import unittest

from game.entities.entity import Entity


class TestEntity(unittest.TestCase):
    def setUp(self) -> None:
        return super().setUp()

    def tearDown(self) -> None:
        return super().tearDown()

    def test_entity_initialization(self):
        entity = Entity(0, 0, 10, 10, (255, 255, 255), 1, 1, True)
        self.assertEqual(entity.rect.x, 0)
        self.assertEqual(entity.rect.y, 0)
        self.assertEqual(entity.rect.width, 10)
        self.assertEqual(entity.rect.height, 10)
        self.assertEqual(entity.speed, 1)
        self.assertEqual(entity.color, (255, 255, 255))
        self.assertEqual(entity.life, 1)
        self.assertEqual(entity.active, True)


if __name__ == "__main__":
    unittest.main()
