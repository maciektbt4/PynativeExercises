import re
str1 = "/*Jon is @developer & musician"
patternReg1 = r"[^\w\s]"
str1 = re.sub(patternReg1, "", str1)
print(str1)