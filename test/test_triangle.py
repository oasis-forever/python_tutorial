import unittest
import sys
sys.path.append("../lib")
from triangle import Triangle

class TestTriangle(unittest.TestCase):
    # Return dimension
    def test_area(self):
        triangle = Triangle(100, 30)
        self.assertEqual(1500, triangle.area())

if __name__ == "__main__":
    unittest.main()
