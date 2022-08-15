def calculateExponent(x,y):
    exponent = 1
    for i in range(1,y+1):
        exponent *= x
    return exponent

print(calculateExponent(2,1))
print(calculateExponent(5,0))