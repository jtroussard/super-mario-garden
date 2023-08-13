import unittest
from game.settings import SCREEN_WIDTH
from game.entities.enemy import Enemy

class TestEnemy(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.enemy = Enemy(0, 0)

    def tearDown(self) -> None:
        super().tearDown()

    def test_enemy_initialization(self):
        self.assertEqual(self.enemy.rect.x, 0)
        self.assertEqual(self.enemy.rect.y, 0)
        self.assertEqual(self.enemy.rect.width, 30)
        self.assertEqual(self.enemy.rect.height, 30)
        self.assertEqual(self.enemy.speed, 1)
        self.assertEqual(self.enemy.color, (255, 0, 0))
        self.assertEqual(self.enemy.life, 1)
        self.assertEqual(self.enemy.active, False)
        self.assertEqual(self.enemy.released, False)

    def test_enemy_movement(self):
        expected = self.enemy.rect.y + self.enemy.speed
        self.enemy.released = True
        self.enemy.active = True
        self.enemy.rect.x = SCREEN_WIDTH/2
        self.enemy.rect.y = 0
        self.enemy.move()
        self.assertTrue(self.enemy.rect.y == expected)

    def test_enemy_repr(self):
        expected = "Enemy\n\tposition:(0, 0)\n\
            speed: 1\n------"
        self.assertEqual(self.enemy.__repr__(), expected)

if __name__ == "__main__":
    unittest.main()
