def printDevisibleBy5(list):
    print("Given list is %s" % list)
    print("Devisible by 5 are elements:")
    for el in list:
        if el % 5 == 0:
            print(el)

x_list = [10, 20, 33, 46, 55, 155, 135, 201, 684]
printDevisibleBy5(x_list)