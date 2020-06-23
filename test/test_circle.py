import unittest
import sys
sys.path.append("../lib")
from circle import Circle

class TestCircle(unittest.TestCase):
    # Return pi
    def test_area(self):
        circle = Circle(29)
        self.assertEqual(2642.079421669016, circle.area())

if __name__ == "__main__":
    unittest.main()
