class Shape:                                                #Super Class
    def __init__(self,color,filled):
        self.color = color
        self.filled = filled
    def describe(self):
        print(f"This is a {self.color} coloured shape")

    def FoNF(self):
        print(f"It is {'filled' if self.filled else 'not filled'}")
    
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color,filled)
        self.radius = radius
    def describe(self):
        print(f"This is a cricle of area {3.14*self.radius*self.radius}cm^2")
        super().describe()
class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color,filled)
        self.width = width
    def describe(self):
        print(f"This is a square of area {self.width*self.width}cm^2")
        super().describe()
class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color,filled)
        self.width = width
        self.height = height
    def describe(self):
        print(f"This is a triangle of area {self.width*self.height*0.5}cm^2")
        super().describe()

circle = Circle("Black", True, 5)
square = Square("White", False, 5)
triangle = Triangle("Red", True,5, 5)

print(circle.color,circle.filled,f"{circle.radius}cm")
print(square.color,square.filled,f"{square.width}cm")
print(triangle.color,triangle.filled,f"{triangle.height}cm",f"{triangle.width}cm")
circle.describe(),circle.FoNF()
square.describe(), square.FoNF()
triangle.describe(), triangle.FoNF()



#If a child's method matches with the parent, child's method will be used