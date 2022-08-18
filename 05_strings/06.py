def mixingChars(string1, string2):
    length1 = len(string1)
    length2 = len(string2)

    # check length of bigger string
    length = length1 if length1 > length2 else length2
    
    # reverse string2
    string2 = string2[::-1]

    result = ""
    for i in range(length):
        if i < length1:
            result += string1[i]
        
        if i < length2:
            result += string2[i]
    return result

s1 = "Abc"
s2 = "Xyz"
print(mixingChars(s1, s2))