def extractIntigerAndReverse(integer):
    numList = []
    for i in integer:
        numList.insert(0,i)

    for num in numList:
        print(num, end = " ")


extractIntigerAndReverse(str(123456789))
