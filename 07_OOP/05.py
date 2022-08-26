class Vehicle:
    color = "white"
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def show(self):
        return f"Name: {self.name}\nMax speed: {self.max_speed}\nMileage: {self.mileage}"

class Bus(Vehicle):
    pass

class Car(Vehicle):
    pass

bus_hope = Bus("hope", 122, "200k")
audi = Car("audi", 264, 2000)

print(bus_hope.show() + f"\nand color is... {bus_hope.color}")
print(audi.show() + f"\nand color is... {audi.color}")