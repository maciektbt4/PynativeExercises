dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

# dict3 = {dict1, dict2}
# print("1) Wrong way to join 2 dictionaries")
# print(dict3)

dict4= {}
dict4.update(dict1)
dict4.update(dict2)
print("2) Correct way to join 2 dictionaries. Easier to remember, but longer.")
print(dict4)

dict5 = {**dict1, **dict2}
print("3) Correct way to join 2 dictionaries. Harder to remember, but shorter.")
print(dict5)