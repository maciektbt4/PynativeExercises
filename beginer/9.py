list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]

resultList = []

for el in list1:
    if el % 2 == 1:
        resultList.append(el)

for el in list2:
    if el % 2 == 0:
        resultList.append(el)

print(f"List 1 {list1}")
print(f"List 2 {list2}")
print(f"Result list is {resultList}")