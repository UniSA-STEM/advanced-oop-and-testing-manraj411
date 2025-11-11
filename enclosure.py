'''
File: enclosure.py
Description: Manages animal housing and cleanliness.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''

class Enclosure:
    """Represents an enclosure that houses animals."""
    def __init__(self, name, env_type, size):
        self._name = name
        self._env_type = env_type
        self._size = size
        self._cleanliness = 100
        self._animals = []

    def add_animal(self, animal):
        """Add an animal if compatible with enclosure type."""
        if self._animals and type(animal) != type(self._animals[0]):
            raise ValueError("Incompatible animal type for this enclosure.")
        self._animals.append(animal)

    def clean(self):
        """Clean the enclosure to full cleanliness."""
        self._cleanliness = 100
        return f"Enclosure '{self._name}' is now clean."

    def report_status(self):
        """Display current animals and enclosure state."""
        status = f"Enclosure '{self._name}' ({self._env_type}) - Cleanliness: {self._cleanliness}%\n"
        if not self._animals:
            status += "No animals currently housed."
        else:
            status += "Animals:\n" + "\n".join([f" - {a.name} ({a.species})" for a in self._animals])
        return status