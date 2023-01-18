import random


class Animal:

    species_list = {"carnivore": ["lion", "coyote", "tiger"], "herbivore": ["elephant", "giraffe", "antelope"]}

    def __init__(self, name, sex, species, PV=10, age=0):
        self.name = name
        self.sex = sex
        self.species = species
        self.PV = PV
        self.age = age

    def eat(self, enclosure):
        if self.species in Animal.species_list["carnivore"]:
            prey = random.choice([p for p in enclosure.in_animal if p.species != self.species])
            self.PV += 5
            prey.PV -= 4
            if prey.PV <= 0:
                enclosure.in_animal.remove(prey)
        else:
            plant = random.choice(enclosure.in_plant)
            self.PV += 3
            plant.eat()
            if plant.PV <= 0:
                enclosure.in_plant.remove(plant)

    def pass_day(self):
        self.PV -= 1
        self.age += 1

    def reproduce(self, enclosure):
        if self.PV > 5:
            partner = random.choice([p for p in enclosure.in_animal if p.species == self.species and p.sex != self.sex])
            if partner:
                new_sex = random.choice(["male", "female"])
                new_animal = Animal(name=self.name, sex=new_sex, species=self.species, PV=10, age=0)
                enclosure.add_animal(new_animal)