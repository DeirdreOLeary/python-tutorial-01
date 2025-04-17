# Simple class
class MyClass:
    x = 5

# Object created from class
p1 = MyClass()
print(p1.x)


# Classes cannot be empty. To avoid errors, use the pass statement
class EmptyClass:
    pass


# Build-in function __init__() is included in all classes
# It is used for operations that are required when the class initiated, e.g. to assign values to object properties
# It is called every time the class is used to create a new object
# self is a reference to the current instance of the class. It must be the first param, but can be named anything
class Person1:
    def __init__(self, name, age):
        self.name = name
        self.age = age

p1 = Person1("John", 36)

# Modify properties
p1.age = 40

print(p1.name)
print(p1.age)


# __str__() controls what should be returned when the class object is represented as a string
class Person2:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def __str__(self):
        return f"{self.name} ({self.age})"
    
p2 = Person2("Ann", 27)

# Note the ifference in what is returned by p1 (i.e. the string representation of the object) & p2
print(p1)
print(p2)


# Classes (& therefore objects) can contain methods, which are functions belonging to the object
class Person3:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        return("Hello, my name is " + self.name)
    
p3 = Person3("Martina", 76)
print(p3.myfunc())
