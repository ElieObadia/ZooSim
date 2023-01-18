import json

from Animal import Animal
from Plant import Plant


class Enclosure:
    def __init__(self):
        self.in_animal = []
        self.in_plant = []

    def add_animal(self, animal):
        self.in_animal.append(animal)

    def add_plant(self, plant):
        self.in_plant.append(plant)

    def report(self):
        report = "The enclosure has after this day :\n"
        report += str(len(self.in_animal)) + "animals\n"
        for animal in self.in_animal:
            report += "{} {} {}\n".format(animal.name, animal.sex, animal.species)
        report += str(len(self.in_plant)) + "plants\n"
        print(report)
        with open("enclosure_report.txt", "w") as file:
            file.write(report)

    def pass_a_day(self):
        for animal in self.in_animal:
            if animal.PV <= 5:
                animal.eat(self)
            if animal.age >= 20:
                self.in_animal.remove(animal)
            animal.reproduce(self)
        for plant in self.in_plant:
            plant.grow()
            if plant.age >= 20:
                self.in_plant.remove(plant)
            plant.reproduce(self)
        for animal in self.in_animal:
            animal.pass_day()
        self.report()

    def save_to_file(self, filename):
        data = {'animals': [], 'plants': []}
        for animal in self.in_animal:
            data['animals'].append(
                {'name': animal.name, 'sex': animal.sex, 'species': animal.species, 'PV': animal.PV, 'age': animal.age})
        for plant in self.in_plant:
            data['plants'].append({'name': plant.name, 'PV': plant.PV, 'age': plant.age})
        with open(filename, 'w') as outfile:
            json.dump(data, outfile)

    def load_state(self, file_name):
        with open(file_name, "r") as file:
            state = json.load(file)
            self.in_animal = [Animal(name=animal["name"], sex=animal["sex"], species=animal["species"], PV=animal["PV"], age=animal["age"]) for animal in state["animals"]]
            self.in_plant = [Plant(name=plant["name"], PV=plant["PV"], age=plant["age"]) for plant in state["plants"]]
