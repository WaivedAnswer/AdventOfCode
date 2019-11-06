import unittest
from Program import *


class MyTestCase(unittest.TestCase):
    def test_origin(self):
        self.assertEqual(geological_index(Coords(0, 0)), 0)

    def test_target(self):
        self.assertEqual(geological_index(target_coords), 0)



if __name__ == '__main__':
    unittest.main()
