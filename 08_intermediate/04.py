ascii_dict = {'A': 65, 'B': 66, 'C': 67, 'D': 68}
ascii_dict_reverse_solution_01 = {}

for key in ascii_dict.keys():
    ascii_dict_reverse_solution_01[ascii_dict[key]] = key

print("Standard dictionary maping: ", ascii_dict)
print("Reversed dictionary maping (solution 01): ", ascii_dict_reverse_solution_01)

ascii_dict_reverse_solution_02 = {value: key for key, value in ascii_dict.items()}
print("Reversed dictionary maping (solution 02, dict comprehensive): ", ascii_dict_reverse_solution_02)


