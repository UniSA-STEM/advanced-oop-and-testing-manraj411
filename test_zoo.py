'''
File: test_zoo.py
Description: Unit tests to validate system functionality.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''

import unittest
from mammal import Mammal
from enclosure import Enclosure

class TestZoo(unittest.TestCase):
    """Unit tests for zoo system."""

    def test_animal_creation(self):
        lion = Mammal("Leo", "Lion", 5, "meat")
        self.assertEqual(lion.name, "Leo")

    def test_enclosure_add_animal(self):
        lion = Mammal("Leo", "Lion", 5, "meat")
        e = Enclosure("Savannah", "Grassland", 400)
        e.add_animal(lion)
        self.assertIn(lion, e._animals)

    def test_incompatible_animal(self):
        from bird import Bird
        lion = Mammal("Leo", "Lion", 5, "meat")
        parrot = Bird("Polly", "Macaw", 2, "seeds")
        e = Enclosure("Mixed", "Forest", 200)
        e.add_animal(lion)
        with self.assertRaises(ValueError):
            e.add_animal(parrot)

if __name__ == "__main__":
    unittest.main()