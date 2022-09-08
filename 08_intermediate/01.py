# Reverse string
string_example = 'My Name is Jessa'
solution_01 = ""
for char in reversed(string_example):
    solution_01+= char
solution_02 = string_example[::-1]
print(string_example)
print(solution_01)
print(solution_02)