def find3MiddleChars(string):
    if len(string) > 3:
        middleIndex = int(len(string) // 2)
        return string[middleIndex-1:middleIndex+2]
    else:
        return string



str1 = "JhonDipPeta"
str2 = "JaSonAy"
str3 = "aaBBcc"

print(find3MiddleChars(str1))
print(find3MiddleChars(str2))
print(find3MiddleChars(str3))