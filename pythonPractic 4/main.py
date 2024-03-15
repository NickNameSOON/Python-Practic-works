class Animal:
    def __init__(self, name, habitat, diet, blood_type):
        self.name = name
        self.habitat = habitat
        self.diet = diet
        self.blood_type = blood_type

    def __str__(self):
        return f"{self.name} is a {self.diet} that lives in the {self.habitat}. It is {self.blood_type}."


class Herbivore(Animal):
    def __init__(self, name, habitat, blood_type):
        super().__init__(name, habitat, "herbivore", blood_type)


class Carnivore(Animal):
    def __init__(self, name, habitat, blood_type):
        super().__init__(name, habitat, "carnivore", blood_type)


class Artiodactyl(Herbivore):
    def __init__(self, name, habitat, blood_type):
        super().__init__(name, habitat, blood_type)


class Bear(Carnivore):
    def __init__(self, name, habitat, blood_type):
        super().__init__(name, habitat, blood_type)


class Snake(Carnivore):
    def __init__(self, name, habitat, blood_type, poisonous):
        super().__init__(name, habitat, blood_type)
        self.poisonous = poisonous


cow = Artiodactyl("Cow", "Grasslands", "warm-blooded")
brown_bear = Bear("Brown Bear", "Forests", "warm-blooded")
grizzly_bear = Bear("Grizzly Bear", "Mountains", "warm-blooded")
cobra = Snake("Cobra", "Deserts", "cold-blooded", True)
adder = Snake("Adder", "Forests", "cold-blooded", False)

print(cow)
print(brown_bear)
print(grizzly_bear)
print(cobra)
print(adder)
