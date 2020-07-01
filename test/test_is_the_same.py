import unittest
import sys
sys.path.append("../lib")
import is_the_same as i
from rider import Rider

class TestIsTheSame(unittest.TestCase):
    def setUp(self):
        self.rider = Rider("Koichi Oguri", 86)

    # Return True if the 2 objects are the same
    def test_is_the_same(self):
        oguri_san = self.rider
        self.assertEqual(True, i.is_the_same(self.rider, oguri_san))

    # Return Flase if the 2 objects are not the same
    def test_is_not_the_same(self):
        another_rider = Rider("Koichi Oguri", 86)
        self.assertEqual(False, i.is_the_same(self.rider, another_rider))

if __name__ == "__main__":
    unittest.main()
