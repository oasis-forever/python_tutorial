import unittest
import sys
sys.path.append("../lib")
from rider import Rider
from horse import Horse

class TestHorse(unittest.TestCase):
    # Return the attributes of a horse and its rider by composition
    def test_horse(self):
        rider = Rider("Koichi Oguri", 86)
        horse = Horse("Oguri Cap", 25, rider)
        self.assertEqual("Oguri Cap", horse.name)
        self.assertEqual(25, horse.age)
        self.assertEqual("Koichi Oguri", horse.rider.name)
        self.assertEqual(86, horse.rider.age)

if __name__ == "__main__":
    unittest.main()
