sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}

# Keys to extract
keys = ["name", "salary"]

# Noice solution
result_dictionary = {key:value for key, value in sample_dict.items() if key=="name" or key == "salary"}
print("Solution 1:")
print(result_dictionary)


# Not so noice but works as well
result_dictionary2 = {}

for key in sample_dict:
    if key == "name" or key == "salary":
        result_dictionary2[key] = sample_dict[key]

print("Solution 2:")
print(result_dictionary2)