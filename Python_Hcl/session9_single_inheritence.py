class Vehicle:
    color = "black"

    def parent_property(self):
        print("Parent property")


class Car(Vehicle):
    # __init__ is the constructor for this class.
    def __init__(self, name, model):
        self.name = name
        self.model = model
        print("Child property")

    def move(self):
        print("Car is moving")


# Create instances at module level
car1 = Car("abc", "C1")
car2 = Car("xyz", "S1")

print(car1.parent_property(), car1.color)
print(car1.name, car1.model)
car1.move()
print(car2.name, car2.model, car2.color)
car2.move()