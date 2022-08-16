from curses.ascii import isalpha, isdigit
from operator import countOf


string1 = "P@#yn26at^&i5ve"

countAlpha = 0
countDigits = 0
countSymbol = 0

for s in string1:
    if s.isalpha():
        countAlpha += 1
    elif s.isdigit():
        countDigits += 1

countSymbol = len(string1) - countAlpha - countDigits

print("Total counts of chars, digits, and symbols\n")
print("Chars = ", countAlpha)
print("Digits = ", countDigits)
print("Symbol = ", countSymbol)