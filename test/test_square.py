import unittest
import sys
sys.path.append("../lib")
from square import Square

class TestSquare(unittest.TestCase):
    # 1. Return sum of perimeter
    def test_calculate_perimeter(self):
        square = Square(40)
        self.assertEqual(160, square.calculate_perimeter())
        # 3. Inherit `Shape` class and call `what_am_i` method
        self.assertEqual("I am a shape.", square.what_am_i())

    # 2. Pass a diff and return sum of perimeter
    def test_change_size(self):
        square = Square(40)
        self.assertEqual(120, square.change_size(-10))

if __name__ == "__main__":
    unittest.main()
