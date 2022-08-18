from audioop import avg
from curses.ascii import isdigit
from statistics import mean


str1 = "PYnative29@#8496"
numbers = []

for s in str1:
    if s.isdigit():
        numbers.append(int(s))

print(f"Sum is: {sum(numbers)} average is: {mean(numbers)}")