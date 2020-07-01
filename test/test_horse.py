import unittest
import sys
sys.path.append("../lib")
from rider import Rider
from horse import Horse

class TestHorse(unittest.TestCase):
    def setUp(self):
        self.rider = Rider("Koichi Oguri", 86)
        self.horse = Horse("Oguri Cap", 25, self.rider)

    # Return the attributes of a horse and its rider by composition
    def test_horse(self):
        self.assertEqual("Oguri Cap", self.horse.name)
        self.assertEqual(25, self.horse.age)
        self.assertEqual("Koichi Oguri", self.horse.rider.name)
        self.assertEqual(86, self.horse.rider.age)

if __name__ == "__main__":
    unittest.main()
