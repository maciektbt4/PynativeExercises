triangleSize = 10

for row in range(1, triangleSize + 1, 1):
    for col in range(row):
        print("*", end = " ")
    print()

for row in range(triangleSize - 1, 0, -1):
    for col in range(row):
        print("*", end = " ")
    print()