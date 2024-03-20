class Animal: #Визначає основні атрибути тварини: name (ім'я) та habitat (середовище проживання).
    def __init__(self, name, habitat):
        self.name = name
        self.habitat = habitat

    def __str__(self):
        return f"{self.name} that lives in the {self.habitat}."


class Herbivore(Animal):    #Наслідується від класу Animal
    def __init__(self, name, habitat):
        super().__init__(name, habitat)
        self.diet = "herbivore"


class Carnivore(Animal):    #Наслідується від класу Animal
    def __init__(self, name, habitat):
        super().__init__(name, habitat)
        self.diet = "carnivore"


class WarmBlooded(Animal):  #Наслідується від класу Animal
    def __init__(self, name, habitat):
        super().__init__(name, habitat)
        self.blood_type = "warm blooded"


class ColdBlooded(Animal):  #Наслідується від класу Animal
    def __init__(self, name, habitat):
        super().__init__(name, habitat)
        self.blood_type = "cold blooded"


class Artiodactyls(Herbivore, WarmBlooded):     #Наслідує від класів Herbivore та WarmBlooded.
    def __init__(self, name, habitat):
        super().__init__(name, habitat)

    def __str__(self):
        return f"{self.name} is a {self.diet} that lives in the {self.habitat}. It is {self.blood_type}."


class Bear(Herbivore, Carnivore, WarmBlooded):      #Наслідує від класів Herbivore, Carnivore та WarmBlooded.
    def __init__(self, name, habitat):
        super().__init__(name, habitat)

    def __str__(self):
        return f"{self.name} is a {self.diet} that lives in the {self.habitat}. It is {self.blood_type}."


class Snakes(Carnivore, ColdBlooded):       #Наслідує від класів Carnivore та ColdBlooded.
    def __init__(self, name, habitat):
        super().__init__(name, habitat)


class PoisonousSnake(Snakes):       #Наслідуються від класу Snakes.
    def __init__(self, name, habitat):
        super().__init__(name, habitat)
        self.isPoisonous = True         #Визначається атрибут отруйність

    def __str__(self):
        return f"{self.name} is a {self.diet} that lives in the {self.habitat}. It is {self.blood_type}."


class NonPoisonousSnake(Snakes):        #Наслідуються від класу Snakes.
    def __init__(self, name, habitat):
        super().__init__(name, habitat)
        self.isPoisonousSnake = False   #Визначається атрибут отруйність

    def __str__(self):
        return f"{self.name} is a {self.diet} that lives in the {self.habitat}. It is {self.blood_type}."


cow = Artiodactyls("Cow", "Grasslands")
brown_bear = Bear("Brown Bear", "Forests")
grizzly_bear = Bear("Grizzly Bear", "Mountains")
cobra = PoisonousSnake("Cobra", "Deserts")
adder = NonPoisonousSnake("Adder", "Forests")

print(cow)
print(brown_bear)
print(grizzly_bear)
print(cobra)
print(adder)
