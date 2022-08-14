numberToCalculateFactorial = int(input("Give me number to calculate factorial: "))
factorialResult = 1

for i in range(1, numberToCalculateFactorial + 1, 1):
    factorialResult *= i

print(f"Result is: {factorialResult}")