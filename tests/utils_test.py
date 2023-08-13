import unittest
import math
from game.utils import degree_to_slope, calculate_face_midpoint


class TestUtils(unittest.TestCase):
    # Parameterized these tests next time you update this util file
    def test_degree_to_slope_0(self):
        degree_in_radians = math.radians(0 - 90)
        expected_result = (math.sin(degree_in_radians), math.cos(degree_in_radians))
        self.assertEqual(degree_to_slope(0), expected_result)

    def test_degree_to_slope_45(self):
        degree_in_radians = math.radians(45 - 90)
        expected_result = (math.sin(degree_in_radians), math.cos(degree_in_radians))
        self.assertEqual(degree_to_slope(45), expected_result)

    def test_degree_to_slope_60(self):
        degree_in_radians = math.radians(60 - 90)
        expected_result = (math.sin(degree_in_radians), math.cos(degree_in_radians))
        self.assertEqual(degree_to_slope(60), expected_result)
        
    def test_degree_to_slope_90(self):
        degree_in_radians = math.radians(90 - 90)
        expected_result = (math.sin(degree_in_radians), math.cos(degree_in_radians))
        self.assertEqual(degree_to_slope(90), expected_result)

    def test_degree_to_slope_135(self):
        degree_in_radians = math.radians(135 - 90)
        expected_result = (math.sin(degree_in_radians), math.cos(degree_in_radians))
        self.assertEqual(degree_to_slope(135), expected_result)

    def test_degree_to_slope_180(self):
        degree_in_radians = math.radians(180 - 90)
        expected_result = (math.sin(degree_in_radians), math.cos(degree_in_radians))
        self.assertEqual(degree_to_slope(180), expected_result)
    
    def test_degree_to_slope_270(self):
        degree_in_radians = math.radians(270 - 90)
        expected_result = (math.sin(degree_in_radians), math.cos(degree_in_radians))
        self.assertEqual(degree_to_slope(270), expected_result)

    # Seriously fuck this test
    def test_calculate_face_midpoint(self):
        class MockEntity:
            def __init__(self, rect, rot):
                self.rect = rect
                self.rot = rot

        width = 10
        entity = MockEntity(rect=MockRect(0, 0, width, 10), rot=180)
        radians = math.radians(entity.rot - 90)
        face_length = width
        
        expected = (
            entity.rect.centerx + (face_length / 2) * math.cos(radians),
            entity.rect.centery - (face_length / 2) * math.sin(radians)
        )
        result = calculate_face_midpoint(entity)
        self.assertEqual(result, expected)


class MockRect:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.centerx = x + width / 2
        self.centery = y + height / 2


if __name__ == "__main__":
    unittest.main()
