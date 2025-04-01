class Rectangle:
    def __init__(self, width, height):
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return f"{self._width:.1f}cm"
    @property
    def height(self):
        return f"{self._height:.1f}cm"

    @width.setter
    def width(self, new_width):
        if new_width > 0:
            self._width = new_width
        else:
            print("The width should be greater than zero")
    @height.setter
    def height(self, new_height):
        if new_height > 0:
            self._height = new_height
        else:
            print("The height should be greater than zero")
    
    @width.deleter
    def width(self):
        print("Deleting the width")
        del self._width
    @height.deleter
    def height(self):
        print("Deleting the height")
        del self._height
rectangle = Rectangle(3,4)
rectangle.height = 1
rectangle.width = 1
del rectangle.height
del rectangle.width
# print(rectangle.height)
# print(rectangle.width)
