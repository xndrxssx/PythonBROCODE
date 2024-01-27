class Rectangles:
    def __init__(self, length,width):
        self.length = length
        self.width = width

class Squares(Rectangles):
    
    def __init__(self, length,width):
        super().__init__(length, width)
        
    def area(self):
        return self.length * self.width
        
class Cube(Rectangles):
    def __init__(self, length, width, height):
        super().__init__(length, width)
        self.height = height
        
    def volume(self):
        return self.length * self.width * self.height
        
        
square = Squares(3,3)
cube = Cube(3,3,3)

print(square.area())
print(cube.volume())
        