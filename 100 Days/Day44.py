# Create a class for a book with attributes like title and author.

class Book:
    title = "Python Tutorial"
    author = "Guido van Rossum"
    
    def __init__(self):
        pass


mybook = Book()
print(mybook.title)
print(mybook.author)