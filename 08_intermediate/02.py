# Solution 01
# lines = []
# with open("02_input.txt", "r") as fp:
#     lines = fp.readlines()

# output_string = ""
# for line in lines:
#     output_string += line.replace("\n", "") + " "

# print(output_string)

# with open("02_output.txt", "w") as fp:
#     fp.write(output_string)

# Solution 02
with open("02_input.txt", "r") as fp:
    lines = fp.read().replace("\n", " ")
    print(lines)
