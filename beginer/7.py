n = int(input("Give number of priamid size: "))
for i in range(n):
    row_string = ""
    for x in range(i+1):
        row_string += str(i+1) + " "
    print(row_string)
