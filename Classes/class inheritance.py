# Base class (i.e. parent)
class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printname(self):
        print(self.firstname, self.lastname)

p = Person('Jane', 'Doe')
p.printname()


# Derived class (i.e. child)
# Pass is used when we don't want to add any additional properties or methods to the class
class Student1(Person):
    pass

c1 = Student1('Bob', 'Howard')
c1.printname()

# Alternative implementation of child
# Adding an __init__() to a child means that it will no longer inherit the parent's __init__() unless an explicit call is made
class Student2(Person):
    def __init__(self, firstname, lastname):
        Person.__init__(self, firstname, lastname)

c2 = Student2('Mina', 'Harker')
c2.printname()

# Alternative implementation of inheritence using super()
class Student3(Person):
    def __init__(self, firstname, lastname, year):
        super().__init__(firstname, lastname)
        self.graduationyear = year
    
    def printgraduation(self):
        print(f"{self.firstname} {self.lastname} graduated in {self.graduationyear}")

c3 = Student3('Jean Luc', 'Picard', '2025')
c3.printgraduation()