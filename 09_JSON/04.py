import json
sampleJson = {"id" : 1, "name" : "value2", "age" : 29}
sortedJson = dict()
keys = sampleJson.keys()
keys = sorted(keys)
for k in keys:
    sortedJson.update({k: sampleJson[k]})

result = json.dumps(sortedJson, indent=4)
print(result)

with open("output/04_output.json", "w") as write_file:
    json.dump(sortedJson, write_file, indent=4)