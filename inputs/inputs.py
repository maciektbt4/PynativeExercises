#--------- ARGS
# from sys import argv

# print(f"total length argv {len(argv)}")
# print(argv)
# sum = 0
# for argument in argv[1:]:
#     sum += int(argument)
# print(sum)

text = input("give me string to justify: ")

print("Left justification ", text.ljust(60," "))
print("Left justification ", text.rjust(60," "))
print("Left justification ", text.center(60," "))