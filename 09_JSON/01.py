import json
data = {"key1" : "value1", "key2" : "value2"}
jsonObject = json.dumps(data)
print(jsonObject)

with open("output/01_output.json", "w") as write_file:
    # json.dump(data, write_file, indent=4, separators=(", ", ": "), sort_keys=True)
    # json.dump(data, write_file, separators=(", ", ": "))
    json.dump(data, write_file)

