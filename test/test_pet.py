import unittest
import sys
sys.path.append("../lib")
from pet import Pet

class TestPet(unittest.TestCase):
    # Define `Pet` which has 3 attributes
    def test_initialize(self):
        pet = Pet("cat", "nana", 18)
        self.assertEqual("cat", pet.species)
        self.assertEqual("nana", pet.name)
        self.assertEqual(18, pet.age)

if __name__ == "__main__":
    unittest.main()
