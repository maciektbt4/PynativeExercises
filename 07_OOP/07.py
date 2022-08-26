class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    def object_type(self):
        return type(self)

school_bus = Bus("School Volvo", 12, 50)
print(school_bus.object_type())