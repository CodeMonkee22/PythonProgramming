class Rectangle:
    pass

class Square(Rectangle):

    def __init__(self, length, width):
        self.length = length
        self.width = width

class Cube(Rectangle):
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height


square = Square(3, 3)
cube = Cube(3, 3, 3)