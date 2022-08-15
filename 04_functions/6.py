def recursiveAddition(num):
    if num > 0:
        return num + recursiveAddition(num -1)
    else:
        return 0

print(str(recursiveAddition(10)))