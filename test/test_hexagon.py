import unittest
import sys
sys.path.append("../lib")
from hexagon import Hexagon

class TestHexagon(unittest.TestCase):
    # Return sum of perimeter
    def test_calculate_perimeter(self):
        hexagon = Hexagon(10, 11, 12, 13, 14, 15)
        self.assertEqual(75, hexagon.calculate_perimeter())

if __name__ == "__main__":
    unittest.main()
