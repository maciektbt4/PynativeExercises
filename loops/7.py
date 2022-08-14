maxRange = 10
for row in range(maxRange):
    for column in range(maxRange - row, 0, -1):
        print(column, end= " ")
    print()