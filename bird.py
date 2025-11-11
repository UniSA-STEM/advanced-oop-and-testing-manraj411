'''
File: bird.py
Description: Bird subclass with unique behaviors.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''


from animal import Animal

class Bird(Animal):
    """Represents bird animals."""
    def make_sound(self):
        return f"{self._name} chirps melodiously."

    def fly(self):
        return f"{self._name} takes flight gracefully."
