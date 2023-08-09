import unittest
from game.entities.bullet import Bullet
from game.settings import COLORS

class Testbullet(unittest.TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.bullet = Bullet(0, 0, 0)  # Create an bullet instance for testing

    def tearDown(self) -> None:
        super().tearDown()

    def test_bullet_initialization(self):
        self.assertEqual(self.bullet.rect.x, 0)
        self.assertEqual(self.bullet.rect.y, 0)
        self.assertEqual(self.bullet.rect.width, 8)
        self.assertEqual(self.bullet.rect.height, 8)
        self.assertEqual(self.bullet.speed, 3)
        self.assertEqual(self.bullet.color, COLORS.get("ORANGE"))
        self.assertEqual(self.bullet.life, 1)
        self.assertEqual(self.bullet.active, True)

    # Important note: 0 degrees is south
    # TODO: I am a little tired but this should most definitely be a parametrized test
    # TODO: Need to fix this test so that bullets are not allowed in this direction
    def test_bullet_move_0_degree(self):
        self.bullet.move()
        self.assertEqual(self.bullet.rect.x, 0)
        self.assertEqual(self.bullet.rect.y, 3)

    def test_bullet_move_45_degree(self):
        self.bullet.angle += 45
        self.bullet.move()
        self.assertEqual(self.bullet.rect.x, 2)
        self.assertEqual(self.bullet.rect.y, 2)

    def test_bullet_move_90_degree(self):
        self.bullet.angle += 90
        self.bullet.move()
        self.assertEqual(self.bullet.rect.x, 3)
        self.assertEqual(self.bullet.rect.y, 0)

    def test_bullet_move_135_degree(self):
        self.bullet.angle += 135
        self.bullet.move()
        self.assertEqual(self.bullet.rect.x, 2)
        self.assertEqual(self.bullet.rect.y, -2)

    def test_bullet_move_180_degree(self):
        self.bullet.angle += 180
        self.bullet.move()
        self.assertEqual(self.bullet.rect.x, 0)
        self.assertEqual(self.bullet.rect.y, -3)

    def test_bullet_move_225_degree(self):
        self.bullet.angle += 225
        self.bullet.move()
        self.assertEqual(self.bullet.rect.x, -2)
        self.assertEqual(self.bullet.rect.y, -2)

    def test_bullet_move_270_degree(self):
        self.bullet.angle += 270
        self.bullet.move()
        self.assertEqual(self.bullet.rect.x, -3)
        self.assertEqual(self.bullet.rect.y, 0)

if __name__ == "__main__":
    unittest.main()
