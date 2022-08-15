
n = int(input("Define square size: "))

a = "*" * n
b = "*" + " "* (n-2) + "*"

for i in range(n):
    if i == 0 or i ==n-1:
        print(a)
    else:
        print(b)