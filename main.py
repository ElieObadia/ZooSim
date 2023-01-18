from Animal import Animal
from Enclosure import Enclosure
from Plant import Plant

if __name__ == "__main__":
    enclosure = Enclosure()
    lion = Animal("Lion", "male", "carnivore")
    giraffe = Animal("Giraffe", "female", "herbivore")
    rose = Plant()
    enclosure.add_animal(lion)
    enclosure.add_animal(giraffe)
    enclosure.add_plant(rose)
    enclosure.pass_a_day()
    enclosure.save_state("enclosure_state.json")