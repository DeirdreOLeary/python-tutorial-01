# Create a class hierarchy for different shapes (circle, square, triangle).

# Base class
class Shape:
    pass
    

# Derived classes
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return (self.radius ** 2) * 3.14


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length * self.length
    

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return self.base * self.height * 0.5


c = Circle(2)
print(c.area())

s = Square(5)
print(s.area())

t = Triangle(2, 5)
print(t.area())