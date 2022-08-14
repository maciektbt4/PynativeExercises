number = 0.0
list = []
for n in range(1,6):
    number = float(input("Give me float number {0}: ".format(n)))
    list.append(number)

print(list)
print(sum(list[-2:]))