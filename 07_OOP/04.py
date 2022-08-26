class Vehicle:
    def __init__(self, name, max_speed, mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage

    def seating_capacity(self, capacity):
        return f"The seating capacity of a {self.name} is {capacity} passengers"

# Solution 1
# class Bus(Vehicle):
#     def __init__(self, name, max_speed, mileage, capacity =50):
#         super().__init__(name, max_speed, mileage)
#         self.capacity = capacity
    
#     def seating_capacity(self):
#         return super().seating_capacity(self.capacity)

# bus_hope = Bus("hope", 123, 12341)
# print(bus_hope.seating_capacity())

# bus_hope.capacity = 65
# print(bus_hope.seating_capacity())

# Solution 2

class Bus(Vehicle):
    def seating_capacity(self, capacity = 50):
        return super().seating_capacity(capacity)

bus_hope = Bus("hope", 123, 12341)
print(bus_hope.seating_capacity())
