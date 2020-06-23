import unittest
import sys
sys.path.append("../lib")
import is_the_same as i
from rider import Rider

class TestIsTheSame(unittest.TestCase):
    # Return True if the 2 objects are the same
    def test_is_the_same(self):
        rider = Rider("Koichi Oguri", 86)
        oguri_san = rider
        self.assertEqual(True, i.is_the_same(rider, oguri_san))

    # Return Flase if the 2 objects are not the same
    def test_is_not_the_same(self):
        rider1 = Rider("Koichi Oguri", 86)
        rider2 = Rider("Koichi Oguri", 86)
        self.assertEqual(False, i.is_the_same(rider1, rider2))

if __name__ == "__main__":
    unittest.main()
