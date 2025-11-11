'''
File: filename.py
Description: A brief description of this Python module.
Author: Billy Bizilis
ID: 110100110
Username: bizvy001
This is my own work as defined by the University's Academic Integrity Policy.
'''

from abc import ABC, abstractmethod
from datetime import datetime
from health_record import HealthRecord

class Animal(ABC):
    def __init__(self, name: str, species: str, age: int, diet: str):
        if not name or not species or age < 0:
            raise ValueError("Invalid animal data provided.")
        self._name = name
        self._species = species
        self._age = age
        self._diet = diet
        self._health_records = []

    @property
    def name(self):
        return self._name

    @property
    def species(self):
        return self._species

    def add_health_record(self, description: str, severity: str):
        record = HealthRecord(datetime.now(), description, severity)
        self._health_records.append(record)

    def get_health_report(self):
        if not self._health_records:
            return f"{self._name} has no recorded health issues."
        report = f"Health Report for {self._name}:\n"
        for record in self._health_records:
            report += f"- {record}\n"
        return report

    @abstractmethod
    def make_sound(self):
        pass

    def eat(self):
        return f"{self._name} the {self._species} is eating {self._diet}."

    def sleep(self):
        return f"{self._name} is sleeping peacefully."
