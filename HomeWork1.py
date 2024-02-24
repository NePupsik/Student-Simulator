class Animal:
    def __init__(self, name, species, legs):
        self.name = name
        self.species = species
        self.legs = legs
    def voice(self):
        print(f"{self.name} is speaking")
    def move(self):
        print(f"{self.species} is moving")
class Dog(Animal):
    def __init__(self, breed, name, species, legs):
        super().__init__(breed, name, species, legs)
        self.breed = "breed"
    def bark(self):
        print(f"{self.name}{self.species} is barking, his breed is {self.breed}")
class Bird(Animal):
    def __init__(self, wingspan, name, species, legs):
        super().__init__(wingspan, name, species, legs)
        self.wingspan = "wingspan"
    def fly(self):
        print(f"{self.name}{self.species} is flying, wingspan = {self.wingspan}")

bird = Bird(wingspan = 185, name = "Lebed", species = "Swan", legs = 2)
print(bird)
bird.fly()

dog = Dog(breed="doggy", name = "Bobik", species = "Barker", legs=4)
print(dog)
dog.bark()