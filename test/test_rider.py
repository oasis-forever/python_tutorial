import unittest
import sys
sys.path.append("../lib")
from rider import Rider

class TestRider(unittest.TestCase):
    # Return the attributes of a horse and its rider by composition
    def test_horse(self):
        rider = Rider("Koichi Oguri", 86)
        self.assertEqual("Koichi Oguri", rider.name)
        self.assertEqual(86, rider.age)

if __name__ == "__main__":
    unittest.main()
