'''
File: staff.py
Description: Defines zookeeper and veterinarian roles.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod

class Staff(ABC):
    """Base class for all zoo staff."""
    def __init__(self, name: str, role: str):
        self._name = name
        self._role = role

    @abstractmethod
    def perform_duty(self):
        pass


class Zookeeper(Staff):
    """Responsible for feeding and cleaning."""
    def perform_duty(self):
        return f"{self._name} is feeding and cleaning animal enclosures."

    def feed_animal(self, animal):
        """Feed a specific animal."""
        return f"{self._name} feeds {animal.name} ({animal.species})."


class Veterinarian(Staff):
    """Responsible for health checks and treatments."""
    def perform_duty(self):
        return f"{self._name} is checking animal health."

    def treat_animal(self, animal, notes):
        """Treat the most recent health issue."""
        if not animal.health_records:
            return f"No health records found for {animal.name}."
        animal.health_records[-1].add_treatment(notes)
        return f"{self._name} treated {animal.name} with notes: {notes}."
