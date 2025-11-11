'''
File: animal.py
Description: Abstract base class for all animals.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from datetime import datetime
from health_record import HealthRecord

class Animal(ABC):
    """Base class for all animals in the zoo."""
    def __init__(self, name: str, species: str, age: int, diet: str):
        if not name or not species or age < 0:
            raise ValueError("Invalid animal data provided.")
        self._name = name
        self._species = species
        self._age = age
        self._diet = diet
        self._health_records = []  # Stores animal health history

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    def add_health_record(self, description: str, severity: str):
        """Add a new health issue for this animal."""
        record = HealthRecord(datetime.now(), description, severity)
        self._health_records.append(record)

    def get_health_report(self):
        """Return a formatted string of all health issues."""
        if not self._health_records:
            return f"{self._name} has no recorded health issues."
        report = f"Health Report for {self._name}:\n"
        for record in self._health_records:
            report += f"- {record}\n"
        return report

    @abstractmethod
    def make_sound(self):
        """Each animal subclass must implement its sound."""
        pass

    def eat(self):
        return f"{self._name} the {self._species} is eating {self._diet}."

    def sleep(self):
        return f"{self._name} is sleeping peacefully."
