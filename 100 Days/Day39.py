# Create a class for a simple car with methods like start and stop.

class Car:
    def __init__(self, model, id):
        self.model = model
        self.id = id

    def start(self):
        return(f"Car (Model: {self.model}) is starting now.")
    
    def stop(self):
        return(f"Car (Licence plate number: {self.id}) is stopping now.")


c1 = Car("Skoda Elroq", '251-C-1234')
print(c1.start())
print(c1.stop())