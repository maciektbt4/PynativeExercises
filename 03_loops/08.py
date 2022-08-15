listForward = [10, 20, 30, 40, 50]
# for el in range(len(listForward), 0, -1):
#     print(listForward[el - 1])
listReverse = reversed(listForward)
for el in listReverse:
    print(el)