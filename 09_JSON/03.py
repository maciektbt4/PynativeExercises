import json
sampleJson = {"key1": "value1", "key2": "value2", "key3": "value3"}
jsonPrettyToPrint = json.dumps(sampleJson, indent=4, separators=(',', ' = '))
print(jsonPrettyToPrint)