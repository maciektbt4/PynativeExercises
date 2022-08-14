# Print prime numbers from range 25 to 50
from time import time

startTime = time()
start = 25
end = 10050

primeNumberlist = []

for num in range(start, end, 1):
    notPrime = False
    for x in range(2, num, 1):
        if num % x == 0:
            notPrime = True
            break
    if not notPrime:
        primeNumberlist.append(num) 

print(primeNumberlist)
print(f"Time of execution: {time() - startTime}")