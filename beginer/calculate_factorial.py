from math import factorial
from time import time, time_ns

sizeList = (10, 100, 1000, 10000, 10000, 100000, 1000000)
timeExecutionList = []

sum_factorial = 1

for n in sizeList:
    startTime = time()
    for i in range(n):
        sum_factorial *= (i + 1)
    timeExecutionList.append(time() - startTime)

print(f"Execution time list is: {timeExecutionList} in [s]")
#print(f"End time: {time()}")