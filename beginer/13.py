def printAsterixTraingle(noRows):
    for asterix in range(noRows):
        row = "* " * (noRows - asterix)
        print(row)

printAsterixTraingle(int(input("Define number of rows: ")))
#printAsterixTraingle(5)