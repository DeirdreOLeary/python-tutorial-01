# Implement polymorphism with a shape area calculator.

# Derived classes
class Circle():
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (self.radius ** 2) * 3.14
    
    def name(self):
        return "Circle"


class Square():
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    
    def name(self):
        return "Square"
    

class Triangle():
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5
    
    def name(self):
        return "Triangle"


c = Circle(2)
s = Square(5)
t = Triangle(2, 5)

for shape in (c, s, t):
    print(shape.name())