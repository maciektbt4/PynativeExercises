str1 = "Apple"
dictString = {}

for s in str1:
    dictString.update({s: str1.count(s)})

print(dictString)