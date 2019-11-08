import unittest
from Program import *


test_depth = 510
test_target = Coords(10, 10)
subject = CaveSystem(test_target, test_depth)


class MyTestCase(unittest.TestCase):
    def test_origin(self):
        self.assertEqual(subject.geological_index(origin), 0)
        self.assertEqual(subject.erosion(origin), test_depth)
        self.assertEqual(subject.terrain(origin), test_depth % 3)

    def test_target(self):
        self.assertEqual(subject.geological_index(test_target), 0)
        self.assertEqual(subject.erosion(test_target), test_depth)
        self.assertEqual(subject.terrain(test_target), test_depth % 3)

    def test_zero_y(self):
        test_coord = Coords(1, 0)
        self.assertEqual(16807, subject.geological_index(test_coord))
        self.assertEqual(17317, subject.erosion(test_coord))
        self.assertEqual(1, subject.terrain(test_coord))

    def test_zero_x(self):
        test_coord = Coords(0, 1)
        self.assertEqual(48271, subject.geological_index(test_coord))
        self.assertEqual(8415, subject.erosion(test_coord))
        self.assertEqual(0, subject.terrain(test_coord))

    def test_1_1(self):
        test_coord = Coords(1, 1)
        self.assertEqual(145722555, subject.geological_index(test_coord))
        self.assertEqual(1805, subject.erosion(test_coord))
        self.assertEqual(2, subject.terrain(test_coord))

    def test_total_risk(self):
        self.assertEqual(114, subject.get_total_risk())

    def test_CoordMap_size(self):
        coord_map = CoordMap(5)
        self.assertFalse(coord_map.has_item(5))
        self.assertFalse(coord_map.has_item(100))
        self.assertFalse(coord_map.has_item(1000))
        self.assertFalse(coord_map.has_item(10000))


if __name__ == '__main__':
    unittest.main()
