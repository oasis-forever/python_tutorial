import unittest
import sys
sys.path.append("../lib")
from triangle import Triangle

class TestTriangle(unittest.TestCase):
    def setUp(self):
        self.triangle = Triangle(100, 30)

    # Return dimension
    def test_area(self):
        self.assertEqual(1500, self.triangle.area())

if __name__ == "__main__":
    unittest.main()
