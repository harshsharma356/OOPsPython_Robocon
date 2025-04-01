from abc import ABC, abstractclassmethod
class Shape(ABC):
    @abstractclassmethod
    def area(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
    
class Square(Shape):
    def __init__(self, width):
        self.width = width
    def area(self):
        return self.width**2
class Triangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return 0.5*self.width*self.height
    
class Pizza(Circle):
    def __init__(self, toppings, radius):
        super().__init__(radius)
        self.toppings = toppings


shapes = [Circle(4), Square(5), Triangle(5,6), Pizza("Pep",5)]



for shape in shapes:
    print(shape.area())

