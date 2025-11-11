'''
File: main.py
Description: Manages animal housing and cleanliness.
Author: Manraj Singh Randhawa
ID: 110480393
Username: manraj411
This is my own work as defined by the University's Academic Integrity Policy.
'''

from mammal import Mammal
from reptile import Reptile
from bird import Bird
from enclosure import Enclosure
from staff import Zookeeper, Veterinarian

def main():
    """Main demo: create animals, enclosures, and staff."""
    # Create animals
    lion = Mammal("Leo", "Lion", 5, "meat")
    snake = Reptile("Sly", "Python", 3, "rats")
    parrot = Bird("Polly", "Macaw", 2, "seeds")

    # Add a health issue to lion
    lion.add_health_record("Limping on front paw", "Moderate")

    # Create enclosures
    savannah = Enclosure("Savannah Habitat", "Savannah", 500)
    reptile_house = Enclosure("Reptile House", "Tropical", 200)
    aviary = Enclosure("Aviary", "Forest", 150)

    # Assign animals to correct enclosures
    savannah.add_animal(lion)
    reptile_house.add_animal(snake)
    aviary.add_animal(parrot)

    # Create staff
    keeper = Zookeeper("Sam")
    vet = Veterinarian("Dr. Taylor")

    # Demonstrate functionality
    print(keeper.perform_duty())
    print(vet.perform_duty())
    print(keeper.feed_animal(lion))
    print(vet.treat_animal(lion, "Applied antiseptic and rest advised"))
    print(savannah.report_status())
    print(lion.get_health_report())

if __name__ == "__main__":
    main()




