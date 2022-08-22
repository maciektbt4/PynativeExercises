keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]

dictionary = {key:value for key, value in zip(keys, values)} 
print(dictionary)


# Less elegant way to do this
dictionary2 ={}
for i in range (len(keys)):
    dictionary2[keys[i]] = values[i]

print(dictionary2)