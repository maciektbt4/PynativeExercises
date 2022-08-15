#Income tax calculator
def incomeTaxCalculator(income):
    # income > 20k  20%
    if income > 20000:
        income -= 20000
        return income * 0.2 + 1000
    # income > 10k 10%
    elif income > 10000:
        income -= 10000
        return income * 0.1
    else:
    # income up to 10k 0%
        return 0.0



income = float(input("what is your income? : "))
tax = incomeTaxCalculator(income)

print(f"Your tax is: {tax}")


