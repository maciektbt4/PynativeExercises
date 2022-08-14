n = 5
numberToAdd = 0
sum = 0
for num in range(1, n + 1, 1):
    numberToAdd = numberToAdd * 10 + 2
    if (num == n):
        print(numberToAdd, end = "")
    else:
        print(numberToAdd, end = " + ")
    sum += numberToAdd
print(" = {0}".format(sum))