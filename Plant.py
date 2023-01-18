class Plant:
    def __init__(self, PV=10, age =0):
        self.PV = PV
        self.age = age

    def grow(self):
        self.PV += 1
        self.age += 1

    def eat(self):
        self.PV -= 2

    def reproduce(self, enclosure):
        if self.PV >= 10:
            new_plant = Plant(name=self.name, PV=int(self.PV / 2), age=self.age)
            enclosure.add_plant(new_plant)
            self.PV = int(self.PV / 2)