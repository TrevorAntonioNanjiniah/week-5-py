# Activity 2: Polymorphism with Vehicles

class Vehicle:
    def move(self):
        pass  # base method (to be overridden)

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")

# Example usage
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    v.move()   # Polymorphism: same method name, different behavior
