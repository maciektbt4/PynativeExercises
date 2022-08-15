from math import factorial
# from time import time, time_ns

# def calcFactorialAndTimeExec(number, startTime):
#     sum_factorial = 1

#     for i in range(number):
#        sum_factorial *= i + 1
#     return sum_factorial, time() - startTime


# sizeList = (10, 100, 1000, 10000, 10000, 100000, 1000000)
# timeExecutionList = []
# results = []
# timeExecutionListFactorialFunction = []

# for n in sizeList:
#     result, execTime = calcFactorialAndTimeExec(n, time())
#     timeExecutionList.append(execTime)
#     results.append(result)

# for n in sizeList:
#     startTime = time()
#     factorial(n)
#     timeExecutionListFactorialFunction.append(time() - startTime)

# print("Factorial to calculate from following numbers: ", sizeList)   
# print("Times execution for user defined function:\n", timeExecutionList)
# print("Times execution for build in function:\n", timeExecutionListFactorialFunction)

with open("factorial_from_milion.txt","w") as fp:
    fp.writelines(str(factorial(1000000)))
