class Vehicle:
    def __init__(self, name, mileage, capacity):
        self.name = name
        self.mileage = mileage
        self.capacity = capacity

class Bus(Vehicle):
    pass

school_bus = Bus("School Volvo", 12, 50)
xwing = Vehicle("X-wing", "1000 light years", 7)

print(f"{school_bus.name} is instance of Vehicle") if isinstance(school_bus, Vehicle) else print(f"{school_bus.name} is not instance of Vehicle")
print(f"{school_bus.name} is instance of Bus") if isinstance(school_bus, Bus) else print(f"{school_bus.name} is not instance of Bus")

print(f"{xwing.name} is instance of Vehicle") if isinstance(xwing, Vehicle) else print(f"{xwing.name} is not instance of Vehicle")
print(f"{xwing.name} is instance of Bus") if isinstance(xwing, Bus) else print(f"{xwing.name} is not instance of Bus")