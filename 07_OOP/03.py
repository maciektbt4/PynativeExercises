class Vehicle:

    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

class Bus(Vehicle):
    def __init__(self, name, max_speed, mileage, colour):
        super().__init__(name, max_speed, mileage)
        self.colour = colour

    def show(self):
        print(f"Bus named {self.name} and colour {self.colour}, can drive at max speed {self.max_speed} and already has milage {self.mileage}")

bus_hope = Bus(name="Hope", max_speed=200, mileage="120k", colour="yellow")
bus_hope.show()