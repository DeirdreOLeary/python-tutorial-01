# Use class decorators in Python.

# define class as decorator
class AddGoodbye:
    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        result = self.function(*args)
        return f"{result} - goodbye!"


# define function with decorator
@AddGoodbye
def type_something(text):
    return f"{text}"


print(type_something("something something..."))
