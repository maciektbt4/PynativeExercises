import json
from json import JSONEncoder

class Vehicle:
    def __init__(self, name, engine, price):
        self.name = name
        self.engine = engine
        self.price = price

class VehicleEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__


vehicle = Vehicle("Toyota Rav4", "2.5L", 32000)

jsonVehicle = json.dumps(vehicle, cls=VehicleEncoder, indent=4)
print(jsonVehicle)

dictVehicle = json.loads(jsonVehicle)
print(dictVehicle)