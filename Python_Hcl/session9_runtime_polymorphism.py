class Car():
    def get_color(self):
        print("Green")

class Audi(Car):
    def get_color(self):
        print("Red")

class Merc(Car):
    def get_color(self):
        print("Yellow")

# Runtime polymorphism
cars = [Car(), Audi(), Merc()]
for car in cars:
    car.get_color() 