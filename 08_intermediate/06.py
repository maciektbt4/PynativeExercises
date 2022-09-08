# Dictionary
d1 = {'A': 65, 'B': 66, 'C': 67, 'D': 68, 'E': 69, 'F': 70}

# Filter dict using following keys
l1 = ['A', 'C', 'F']

d2 = {key: value for key, value in d1.items() if key in l1}
print("Input dictionary: ", d1)
print("Filtred dictionary: ", d2)