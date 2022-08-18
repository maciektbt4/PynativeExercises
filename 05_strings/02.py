def injectString(string, stringIncjected):
    middleIndex = int(len(string)/2)
    return string[:middleIndex] + stringIncjected + string[middleIndex:]

print(injectString("Ault", "Kelly"))