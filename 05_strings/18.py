import re
import string
str1 = '/*Jon is @developer & musician!!'

# Solution with regex
# reg_pattern = r"[^\w\s]"
# str1 = re.sub(reg_pattern, "#", str1)
# print(str1)

# Solution with string punctionation
resultString = ""
for s in str1:
    isSpecialSign = False
    for char in string.punctuation:
        if s == char:
            resultString += "#"
            isSpecialSign = True
            break
    if not isSpecialSign:
        resultString += s
    
print(resultString)