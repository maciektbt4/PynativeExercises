def printVariables(*args):
    print("Printing values:")
    for el in args:
        print(el)

tuple_2elements = (80, 100)
tuple_3elements = (20, 40, 60)

printVariables(*tuple_3elements)
printVariables(*tuple_2elements)