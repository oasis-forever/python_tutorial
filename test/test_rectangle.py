import unittest
import sys
sys.path.append("../lib")
from rectangle import Rectangle

class TestRectangle(unittest.TestCase):
    # Return sum of perimeter
    def test_ractangle(self):
        rectangle = Rectangle(20, 30)
        self.assertEqual(100, rectangle.calculate_perimeter())
        # 3. Inherit `Shape` class and call `what_am_i` method
        self.assertEqual("I am a shape.", rectangle.what_am_i())

if __name__ == "__main__":
    unittest.main()
