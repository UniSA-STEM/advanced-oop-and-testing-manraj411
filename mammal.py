'''
File: animal.py
Description: Mammal subclass with unique behaviors.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Mammal(Animal):
    """Represents mammal animals."""
    def make_sound(self):
        return f"{self._name} makes a growling sound."

    def feed_milk(self):
        return f"{self._name} is feeding milk to its young."
