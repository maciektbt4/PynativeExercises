number_list = [100, 65, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print(number_list)

over_50 = True
while (over_50):
    over_50 = False
    for number in number_list:    
        if number > 50:
            number_list.remove(number)
            over_50 = True

print(number_list)
