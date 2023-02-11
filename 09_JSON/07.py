import json
from json import JSONDecoder
from collections import namedtuple

def vehicleEncoder(vehicle):
    return namedtuple('X', vehicle.keys())(*vehicle.values())

vehicleJSON = """{ "name": "Toyota Rav4", "engine": "2.5L", "price": 32000 }"""
vehicle  = json.loads(vehicleJSON, object_hook=vehicleEncoder)
print(f"Car type: {vehicle.name}\nEngine size: {vehicle.engine} ")