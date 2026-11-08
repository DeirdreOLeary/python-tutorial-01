# Encapsulation protects your classes from accidental changes or deletions, i.e. to prevent the following:
class Smartphone:
   def __init__(self, brand, os):
       self.brand = brand
       self.os = os

iphone = Smartphone("Apple", "iOS 17")

# Overwrite the iphone operating system to "Android", which shouldn't be allowed!
iphone.os = "Android"
print(iphone.os)


# Note: In python, encapsulation is not enforced. Instead it is supported through conventions & programming practices, e.g.:
    # Access modifiers: naming conventions (_protected, __private, rather than public with no underscore)
    # Getter/setter methods: optional @property decorator for controlled access
    # Data Access: naming conventions


# Using access modifiers
# Protected member (single underscore)
class Tree1:
    def __init__(self, height):
        self._height = height

t1 = Tree1(20)
print(t1._height)

# The protected member (_height) can be changed but devs who are aware of the convention know that they shouldn't.
t1._height = 50
print(t1._height)

# Private member (double underscore)
class Flower:
    def __init__(self, colour):
        self.__colour = colour

# The private member (__colour) cannot be accessed, let alone changed. AttributeError: 'Flower' object has no attribute '__colour'
f = Flower('Red')
print(f.__colour)


# Using getter/setter methods
class Tree2():
    def __init__(self, height):
        self.__height = height
    
    @property
    def height(self):
        return self.__height
    
    @height.getter
    def height(self):
        return f"This tree is {self.__height} meters tall."
    
    @height.setter
    def height(self, new_height):
        if not isinstance(new_height, int):
            raise TypeError("Tree height must be an integer")
        if 0 < new_height <= 116:
            self.__height = new_height
        else:
            raise ValueError("Invalid height for a tree")

# Calls @height.getter to return the custom message
t2 = Tree2(35)
print(t2.height)

# Calls @height.setter to set the height to a valid value
t2.height = 60
print(t2.height)

# Fails with a TypeError: Tree height must be an integer
t2.height = 'Banana'

# However it is stil possible to work around this convention!
t2._Tree2__height = "Gotcha!"
print(t2.height)