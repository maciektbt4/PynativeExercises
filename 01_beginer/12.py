#Print multiplication table
for x in range(1,11):
    row = ""
    for y in range(1,11):
        row += f"{(x * y)} "
    print(row)