listFibonnaci = [0, 1]

while len(listFibonnaci) < 10:
    secondLastNumber = listFibonnaci[-2]
    lastNumber = listFibonnaci[-1]
    listFibonnaci.append(secondLastNumber + lastNumber)

print("10 first elements in Fibonnaci sequance are: {0}".format(listFibonnaci))