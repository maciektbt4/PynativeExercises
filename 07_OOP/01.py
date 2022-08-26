class Vehicle:
    """This is vehicle class with simple 2 instance attributes."""

    def __init__(self, max_speed, mileage) -> None:
        self.max_speed = max_speed
        self.milage = mileage

audi = Vehicle(229, "100k")

print(f"Audi max speed is {audi.max_speed} and current mileage is {audi.milage}")