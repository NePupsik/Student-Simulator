class Shape:
    def __init__(self):
        self.name = "name"
        self.color = "orange"
class Circle(Shape):
    def __init__(self):
        self.radius = "r"
        self.start = True
    def print(self):
        if self.start = True:
            self.area()

    def area(self):
        a = "r * r × π"
        print(a)
class Rectangle(Shape):
    def __init__(self):
        self.length = "length"
        self.width = "width"
        self.start = True

    def print1(self):
        if self.start = True:
            self.area()
    def area(self):
        a = "length * width"
        print(a)

class Triangle(Shape):
    def __init__(self):
        self.base = "base"
        self.height ="height"
        self.start = True

    def print1(self):
        if self.start = True:
            self.area()

    def area(self):
        a = "base * height : 2"
        print(a)