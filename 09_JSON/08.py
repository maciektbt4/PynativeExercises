import json

 
def validateJSON(jsonData):
    try:
        json.load(jsonData)
    except ValueError as err:
        return False
    return True

with open("input/08_input.json", "r") as readFile:
    print("JSON file is valid") if validateJSON(readFile) else print ("JSON file is not valid")