import json
sampleJson = """{"key1": "value1", "key2": "value2"}"""

dict_from_json = json.loads(sampleJson)
print(dict_from_json["key2"])