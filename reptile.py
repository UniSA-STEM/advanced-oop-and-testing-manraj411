'''
File: reptile.py
Description: Reptile subclass with unique behaviors.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''

from animal import Animal

class Reptile(Animal):
    """Represents reptile animals."""
    def make_sound(self):
        return f"{self._name} hisses softly."

    def shed_skin(self):
        return f"{self._name} is shedding its skin."
