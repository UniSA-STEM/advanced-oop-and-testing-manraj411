'''
File: health_record.py
Description: Tracks animal health issues and treatments.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''


class HealthRecord:
    """Stores details of an animal's health issue."""
    def __init__(self, date_reported, description, severity):
        self.date_reported = date_reported
        self.description = description
        self.severity = severity
        self.treatment_notes = None

    def add_treatment(self, notes):
        """Add treatment notes to the record."""
        self.treatment_notes = notes

    def __str__(self):
        base = f"{self.date_reported.strftime('%Y-%m-%d')} - {self.description} (Severity: {self.severity})"
        if self.treatment_notes:
            base += f" | Treatment: {self.treatment_notes}"
        return base
