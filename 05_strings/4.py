str1 = "PyNaTive"
capitalized = ""
lowercases = ""

for s in str1:
    if s.islower():
        lowercases += s
    else:
        capitalized += s

result = lowercases + capitalized
print(result)
