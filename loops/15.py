from unittest import result


my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
resultList = []
# for i in range(0, len(my_list), 1):
#     if i % 2 == 1:
#         resultList.append(my_list[i])
# print(resultList)

for el in my_list[1::2]:
    print(el, end= " ")
print()