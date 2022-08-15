
from pickle import FALSE, TRUE


def compareFirstAndLastElementinList(list):
    print(f"Given list: {list}")
    if list[0] == list[-1]:
        return True
    else:
        return False


numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 25, 10, 34, 75, 100]
print(compareFirstAndLastElementinList(numbers_x))
print(compareFirstAndLastElementinList(numbers_y))