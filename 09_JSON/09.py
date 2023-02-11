import json

listJSON = []
with open("input/09_input.json", "r") as json_file:
    listJSON = json.load(json_file)

# Solution 1
results = [item.get("name") for item in listJSON]

# Solution 2
# for el in listJSON:
#     results.append(el.get("name"))

# Solution 3
# for el in listJSON:
#     dict = el
#     for key, value in dict.items():
#         if key == "name":
#             results.append(value)
print(results)