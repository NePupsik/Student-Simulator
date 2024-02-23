class Animal:
    def __init__(self):
        name = "name"
        species = "species"
        legs = "legs"
    def voice(self):
        pass
    def move(self):
        pass
class Dog(Animal):
    def __init__(self, breed, name, species, legs, bark):
        breed = "breed"
    def bark(self):
        pass
class Bird(Animal):
    def __init__(self, wingspan, name, species, legs, fly):
        wingspan = "wingspan"
    def fly(self):
        pass