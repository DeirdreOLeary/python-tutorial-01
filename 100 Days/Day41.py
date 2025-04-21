# Implement inheritance between classes.

# Base class
class Shape:
    def __init__(self, shape):
        self.shape = shape
    
    def name_of_shape(self):
        return f"This shape is a {self.shape}"
    

# Derived classes
class Circle(Shape):
    def __init__(self, radius, shape = 'circle'):
        Shape.__init__(self, shape)
        self.radius = radius
        self.shape = shape
    
    def area(self):
        return (self.radius ** 2) * 3.14


class Square(Shape):
    def __init__(self, length, shape = 'square'):
        Shape.__init__(self, shape)
        self.length = length
        self.shape = shape

    def area(self):
        return self.length * self.length
    

class Triangle(Shape):
    def __init__(self, base, height, shape = 'triangle'):
        Shape.__init__(self, shape)
        self.base = base
        self.height = height
        self.shape = shape

    def area(self):
        return self.base * self.height * 0.5


c = Circle(2)
print(c.name_of_shape())
print(c.area())

s = Square(5)
print(s.name_of_shape())
print(s.area())

t = Triangle(2, 5)
print(t.name_of_shape())
print(t.area())