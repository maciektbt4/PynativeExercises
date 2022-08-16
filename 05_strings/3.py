def midlleCharInString(string):
    mid = int(len(string)/2)
    return string[mid]

def mixString(string1, string2):
    # Add to result first characters from both strings
    result = string1[0] + string2[0]

    # Add middle char from both strings
    result += midlleCharInString(string1) + midlleCharInString(string2)

    # Add last char from both strings
    result += string1[-1] + string2[-1]
    
    return result

s1 = "America"
s2 = "Japan"

print(mixString(s1, s2))
